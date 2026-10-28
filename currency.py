"""Valyuta kurslari xizmati: CBU (Markaziy bank) kurslari va so'mga konvertatsiya.

cbu.uz O'zbekistondan tashqaridagi serverlarni (Render ham) bloklaydi, shuning uchun
admin CBU kursini /setkurs buyrug'i bilan qo'lda kiritadi. Kurs admin chatidagi
qadalgan (pin) xabarda saqlanadi — Render qayta ishga tushganda ham yo'qolmaydi.
"""
import datetime as dt
import logging
import re
import time

import aiohttp
from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from logistics import admin_ids
from texts import T

CBU_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
CURRENCIES = ("USD", "EUR", "CNY", "RUB", "TRY", "KZT", "KGS", "KRW")
FLAGS = {"USD": "🇺🇸", "EUR": "🇪🇺", "CNY": "🇨🇳", "RUB": "🇷🇺", "TRY": "🇹🇷",
         "KZT": "🇰🇿", "KGS": "🇰🇬", "KRW": "🇰🇷"}


SETKURS_HELP = (
    "✍️ <b>CBU kursini kiritish</b>\n\n"
    "cbu.uz saytidagi bugungi kursni shunday yozing:\n\n"
    "<code>/setkurs USD 11918.98 EUR 13283.70 CNY 1787.60 RUB 148.04 "
    "TRY 239.47 KZT 26.12 KGS 136.25 KRW 8.32</code>\n\n"
    "• Faqat o'zgarganlarini yozsangiz ham bo'ladi (masalan: <code>/setkurs USD 11925</code>)\n"
    "• Sana avtomatik bugungi kun bo'ladi. Boshqa sana: oxiriga <code>29.10.2026</code> qo'shing"
)


class Conv(StatesGroup):
    amount = State()


# ---------- CBU kurslari (1 soat keshlanadi) ----------
_cache = {"rates": None, "ts": 0}

FALLBACK_URL = "https://open.er-api.com/v6/latest/UZS"
# Ba'zi saytlar aiohttp ning standart User-Agent'ini bloklaydi
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DCGinfoBot/1.0)", "Accept": "application/json"}


async def _fetch_json(url: str, timeout: int = 20):
    async with aiohttp.ClientSession(headers=HEADERS) as s:
        async with s.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as r:
            r.raise_for_status()
            return await r.json(content_type=None)


# CBU javob bermasa, 3 soat qayta urinmaymiz (aks holda har so'rov kutib qoladi)
_cbu_down_until = 0.0


async def _from_cbu() -> dict:
    global _cbu_down_until
    if time.time() < _cbu_down_until:
        raise RuntimeError("CBU yaqinda javob bermadi")
    try:
        data = await _fetch_json(CBU_URL, timeout=6)
    except Exception:
        _cbu_down_until = time.time() + 3 * 3600
        raise
    rates = {x["Ccy"]: {"rate": float(x["Rate"]), "diff": float(x["Diff"] or 0),
                        "nominal": int(x["Nominal"]), "date": x["Date"], "src": "cbu"}
             for x in data if x["Ccy"] in CURRENCIES}
    if "USD" not in rates:
        raise ValueError("CBU javobida USD yo'q")
    return rates


async def _from_fallback() -> dict:
    """Zaxira manba: bozor kursi (CBU dan biroz farq qilishi mumkin), kunlik o'zgarishsiz."""
    data = await _fetch_json(FALLBACK_URL)
    per_uzs = data["rates"]
    date = time.strftime("%d.%m.%Y", time.gmtime(data["time_last_update_unix"]))
    return {c: {"rate": 1 / per_uzs[c], "diff": None, "nominal": 1, "date": date, "src": "alt"}
            for c in CURRENCIES if per_uzs.get(c)}


# ---------- Admin qo'lda kiritgan CBU kursi ----------
MANUAL_TAG = "#DCGKURS"
_manual = {"rates": None}  # {"date": "28.10.2026", "rates": {"USD": 11918.98, ...}}


def _from_manual_sync() -> dict:
    m = _manual["rates"]
    if not m:
        raise ValueError("Qo'lda kiritilgan kurs yo'q")
    return {c: {"rate": v, "diff": None, "nominal": 1, "date": m["date"], "src": "manual"}
            for c, v in m["rates"].items() if c in CURRENCIES}


async def _from_manual() -> dict:
    return _from_manual_sync()


def parse_rates(text: str) -> dict:
    """«USD 11 918,98 EUR 13283.70» -> {"USD": 11918.98, "EUR": 13283.7}"""
    found = {}
    for ccy, num in re.findall(r"\b([A-Za-z]{3})\b\s*[=:]?\s*(\d[\d ]*(?:[.,]\d+)?)", text):
        ccy = ccy.upper()
        if ccy in CURRENCIES:
            found[ccy] = float(num.replace(" ", "").replace(",", "."))
    return found


def manual_text(m: dict) -> str:
    """Admin chatida qadalib turadigan xabar (bot shu xabardan kursni qayta o'qiydi)."""
    lines = [f"{c} {m['rates'][c]}" for c in CURRENCIES if c in m["rates"]]
    return ("💾 <b>Saqlangan CBU kursi</b> — bu xabarni o'chirmang va pin'dan olmang!\n\n"
            f"{MANUAL_TAG} {m['date']}\n" + "\n".join(lines))


def parse_manual(text: str) -> dict | None:
    match = re.search(MANUAL_TAG + r"\s+(\d{2}\.\d{2}\.\d{4})", text or "")
    if not match:
        return None
    rates = parse_rates(text[match.end():])
    return {"date": match.group(1), "rates": rates} if rates else None


async def load_manual(bot: Bot):
    """Bot ishga tushganda adminlar chatidagi qadalgan xabarlardan eng yangi kursni o'qiydi."""
    found = []
    for admin in admin_ids():
        try:
            chat = await bot.get_chat(admin)
            m = parse_manual(chat.pinned_message.text if chat.pinned_message else "")
            if m:
                found.append(m)
        except Exception as e:
            logging.warning("Admin (%s) chatidan kursni o'qib bo'lmadi: %r", admin, e)
    if found:
        _manual["rates"] = max(found, key=lambda m: dt.datetime.strptime(m["date"], "%d.%m.%Y"))
        _cache["rates"] = None
        logging.info("Qo'lda kiritilgan kurs yuklandi: %s", _manual["rates"]["date"])


async def get_rates() -> dict | None:
    """{"USD": {"rate": 11861.96, "diff": 23.04, "nominal": 1, "date": "27.10.2026", "src": "cbu"}, ...}"""
    if _cache["rates"] and time.time() - _cache["ts"] < 3600:
        return _cache["rates"]
    for source in (_from_cbu, _from_manual, _from_fallback):
        try:
            rates = await source()
            _cache.update(rates=rates, ts=time.time())
            return rates
        except Exception as e:
            logging.warning("Kurslarni olib bo'lmadi (%s): %r", source.__name__, e)
    return _cache["rates"]


def fmt(n: float, digits: int = 2) -> str:
    s = f"{n:,.{digits}f}".replace(",", " ")
    return s.rstrip("0").rstrip(".") if digits else s


def rates_text(lang: str, rates: dict) -> str:
    t = T[lang]
    lines = []
    for c in CURRENCIES:
        if c not in rates:
            continue
        r = rates[c]
        line = f"{FLAGS[c]} {r['nominal']} {c} = <b>{fmt(r['rate'])}</b> {t['cur_sum']}"
        if r["diff"] is not None:
            arrow = "🟢 ▲" if r["diff"] > 0 else "🔴 ▼" if r["diff"] < 0 else "⚪️"
            line += f"  {arrow} {fmt(abs(r['diff']))}"
        lines.append(line)
    first = next(iter(rates.values()))
    source = {"cbu": t["cur_source"], "manual": t["cur_source_manual"]}.get(first["src"], t["cur_source_alt"])
    return t["cur_title"].format(date=first["date"]) + "\n\n" + "\n".join(lines) + "\n\n" + source


# ---------- Klaviaturalar ----------
def rates_kb(lang):
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["cur_btn_convert"], callback_data="cur:conv", style="success")],
        [InlineKeyboardButton(text=t["cur_btn_refresh"], callback_data="cur:refresh", style="primary")],
    ])

def pick_kb(lang):
    buttons = [InlineKeyboardButton(text=f"{FLAGS[c]} {c}", callback_data=f"cur:pick:{c}", style="primary")
               for c in CURRENCIES]
    rows = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def build_router(get_lang, main_kb, cancel_kb):
    """(router, start) qaytaradi: start — asosiy menyudagi «Valyuta kursi» tugmasi uchun."""
    router = Router(name="currency")

    async def send_rates(m: Message, lang: str, edit: bool = False):
        rates = await get_rates()
        if not rates:
            return await m.answer(T[lang]["cur_error"])
        text = rates_text(lang, rates)
        if edit:
            try:
                return await m.edit_text(text, reply_markup=rates_kb(lang))
            except Exception:
                return  # matn o'zgarmagan bo'lsa Telegram xato beradi
        await m.answer(text, reply_markup=rates_kb(lang))

    # ----- Asosiy menyudan yoki /kurs buyrug'i -----
    @router.message(F.text.in_({"/kurs", "/rates"}))
    async def currency_start(m: Message, state: FSMContext):
        await state.clear()
        await send_rates(m, get_lang(m.from_user.id))

    # ----- Admin: CBU kursini qo'lda kiritish -----
    @router.message(Command("setkurs"))
    async def set_rates(m: Message, command: CommandObject, bot: Bot):
        admins = admin_ids()
        if m.from_user.id not in admins:
            return await m.answer(f"⛔️ Bu buyruq faqat adminlar uchun.\nSizning ID: <code>{m.from_user.id}</code>")
        text = command.args or ""
        date = re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
        rates = parse_rates(text.replace(date.group(0), " ") if date else text)
        if not rates:
            return await m.answer(SETKURS_HELP)
        tashkent = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=5)
        old = _manual["rates"]["rates"] if _manual["rates"] else {}
        new = {"date": date.group(0) if date else tashkent.strftime("%d.%m.%Y"), "rates": {**old, **rates}}

        saved = await m.answer(manual_text(new))
        await bot.pin_chat_message(m.chat.id, saved.message_id, disable_notification=True)
        _manual["rates"] = new
        _cache.update(rates=_from_manual_sync(), ts=time.time())

        lines = "\n".join(f"{FLAGS[c]} {c} = <b>{fmt(new['rates'][c])}</b> so'm"
                          for c in CURRENCIES if c in new["rates"])
        missing = [c for c in CURRENCIES if c not in new["rates"]]
        note = f"\n\n⚠️ Kiritilmagan: {', '.join(missing)}" if missing else ""
        await m.answer(f"✅ <b>Kurs saqlandi</b> ({new['date']})\n\n{lines}{note}")

    @router.callback_query(F.data == "cur:refresh")
    async def refresh(c: CallbackQuery):
        await send_rates(c.message, get_lang(c.from_user.id), edit=True)
        await c.answer(T[get_lang(c.from_user.id)]["cur_refreshed"])

    # ----- Konvertatsiya: valyuta -> so'm -----
    @router.callback_query(F.data == "cur:conv")
    async def conv_start(c: CallbackQuery):
        await c.message.answer(T[get_lang(c.from_user.id)]["cur_pick"],
                               reply_markup=pick_kb(get_lang(c.from_user.id)))
        await c.answer()

    @router.callback_query(F.data.startswith("cur:pick:"))
    async def conv_pick(c: CallbackQuery, state: FSMContext):
        lang = get_lang(c.from_user.id)
        ccy = c.data.split(":")[2]
        await state.set_state(Conv.amount)
        await state.update_data(ccy=ccy)
        await c.message.edit_text(f"✅ {FLAGS[ccy]} {ccy}")
        await c.message.answer(T[lang]["cur_ask_amount"].format(ccy=ccy), reply_markup=cancel_kb(lang))
        await c.answer()

    @router.message(Conv.amount)
    async def conv_amount(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        t = T[lang]
        try:
            amount = float((m.text or "").strip().replace(" ", "").replace(",", "."))
            assert 0 < amount < 1e12
        except Exception:
            return await m.answer(t["cur_bad_amount"])
        rates = await get_rates()
        if not rates:
            await state.clear()
            return await m.answer(t["cur_error"], reply_markup=main_kb(lang))
        ccy = (await state.get_data())["ccy"]
        if ccy not in rates:
            await state.clear()
            return await m.answer(t["cur_error"], reply_markup=main_kb(lang))
        r = rates[ccy]
        uzs = amount * r["rate"] / r["nominal"]
        await state.clear()
        await m.answer(t["cur_result"].format(amount=fmt(amount), ccy=ccy, flag=FLAGS[ccy],
                                              uzs=fmt(uzs, 0), rate=fmt(r["rate"]),
                                              date=r["date"],
                                              src="open.er-api.com" if r["src"] == "alt" else "cbu.uz"),
                       reply_markup=main_kb(lang))

    return router, currency_start
