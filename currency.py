"""Valyuta kurslari xizmati: CBU (Markaziy bank) kurslari va so'mga konvertatsiya."""
import logging
import time

import aiohttp
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from texts import T

CBU_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
CURRENCIES = ("USD", "EUR", "RUB", "CNY", "KRW", "KZT")
FLAGS = {"USD": "🇺🇸", "EUR": "🇪🇺", "RUB": "🇷🇺", "CNY": "🇨🇳", "KRW": "🇰🇷", "KZT": "🇰🇿"}


class Conv(StatesGroup):
    amount = State()


# ---------- CBU kurslari (1 soat keshlanadi) ----------
_cache = {"rates": None, "ts": 0}

FALLBACK_URL = "https://open.er-api.com/v6/latest/UZS"
# Ba'zi saytlar aiohttp ning standart User-Agent'ini bloklaydi
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DCGinfoBot/1.0)", "Accept": "application/json"}


async def _fetch_json(url: str):
    async with aiohttp.ClientSession(headers=HEADERS) as s:
        async with s.get(url, timeout=aiohttp.ClientTimeout(total=20)) as r:
            r.raise_for_status()
            return await r.json(content_type=None)


async def _from_cbu() -> dict:
    data = await _fetch_json(CBU_URL)
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


async def get_rates() -> dict | None:
    """{"USD": {"rate": 11861.96, "diff": 23.04, "nominal": 1, "date": "27.10.2026", "src": "cbu"}, ...}"""
    if _cache["rates"] and time.time() - _cache["ts"] < 3600:
        return _cache["rates"]
    for source in (_from_cbu, _from_cbu, _from_fallback):
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
    source = t["cur_source"] if first["src"] == "cbu" else t["cur_source_alt"]
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


def build_router(get_lang, main_kb, cancel_kb) -> Router:
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

    # ----- Xizmatlar menyusidan yoki /kurs buyrug'i -----
    @router.callback_query(F.data == "svc:currency")
    async def currency_start(c: CallbackQuery, state: FSMContext):
        await state.clear()
        await send_rates(c.message, get_lang(c.from_user.id))
        await c.answer()

    @router.message(F.text.in_({"/kurs", "/rates"}))
    async def currency_cmd(m: Message, state: FSMContext):
        await state.clear()
        await send_rates(m, get_lang(m.from_user.id))

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
        r = rates[ccy]
        uzs = amount * r["rate"] / r["nominal"]
        await state.clear()
        await m.answer(t["cur_result"].format(amount=fmt(amount), ccy=ccy, flag=FLAGS[ccy],
                                              uzs=fmt(uzs, 0), rate=fmt(r["rate"]),
                                              date=r["date"],
                                              src="cbu.uz" if r["src"] == "cbu" else "open.er-api.com"),
                       reply_markup=main_kb(lang))

    return router
