"""DCGCargo — Telegram bot."""
import asyncio
import logging
import os
import time
import datetime as dt
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile)
from dotenv import load_dotenv

import rates as R
import logistics
import currency
import certificate
import trade
import admin
import db
from calculator import calculate
from texts import T

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
_tok_file = Path(__file__).with_name("token.txt")
if not TOKEN and _tok_file.exists():
    TOKEN = _tok_file.read_text(encoding="utf-8-sig").strip() or None
if TOKEN and ":" not in TOKEN:
    TOKEN = None

# Qo'llab-quvvatlash: admin akkaunti va telefoni (Render'da env orqali ham o'zgartirsa bo'ladi)
SUPPORT_USERNAMES = [u.strip().lstrip("@") for u in
                     os.getenv("SUPPORT_USERNAMES", "Dcgadmin2229,DCG_manager").split(",") if u.strip()]
SUPPORT_PHONE = os.getenv("SUPPORT_PHONE", "+998 55 500 11 13")

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


# ---------- Foydalanuvchi tili ----------
# Tillar bazada saqlanadi; tez o'qish uchun xotirada ham turadi (bot ishga tushganda yuklanadi)
USERS: dict = {}

def get_lang(uid: int) -> str:
    return USERS.get(str(uid), "uz")

async def set_lang(user, lang: str):
    USERS[str(user.id)] = lang
    await db.set_lang(user, lang)


# ---------- Mijozlar bazasi: har bir foydalanuvchi faolligini yozib boradi ----------
_last_touch: dict = {}

async def track_user(handler, event, data):
    user = data.get("event_from_user")
    if user and not user.is_bot:
        t = time.monotonic()
        if t - _last_touch.get(user.id, -1e9) > 600:  # bazaga ko'pi bilan 10 daqiqada bir marta
            _last_touch[user.id] = t
            try:
                await db.touch_user(user)
            except Exception as e:
                logging.error("Mijozni bazaga yozib bo'lmadi (%s): %r", user.id, e)
    return await handler(event, data)

dp.message.outer_middleware(track_user)
dp.callback_query.outer_middleware(track_user)


# ---------- USD kursi (CBU) ----------
async def usd_rate() -> float:
    """Valyuta xizmati bilan bir xil manba (CBU, zaxira: open.er-api.com)."""
    rates = await currency.get_rates()
    if rates and "USD" in rates:
        return rates["USD"]["rate"]
    return R.FALLBACK_USD_RATE


# ---------- Klaviaturalar ----------
def main_kb(lang):
    t = T[lang]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=t["btn_trade"], style="success")],
        [KeyboardButton(text=t["btn_calc"], style="primary")],
        [KeyboardButton(text=t["btn_cert"], style="primary")],
        [KeyboardButton(text=t["btn_logistics"], style="success"),
         KeyboardButton(text=t["btn_currency"], style="success")],
        [KeyboardButton(text=t["btn_support"])],
        [KeyboardButton(text=t["btn_info"]), KeyboardButton(text=t["btn_lang"])],
    ])

def support_kb(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{T[lang]['support_btn_write']} @{u}",
                              url=f"https://t.me/{u}", style="primary")]
        for u in SUPPORT_USERNAMES
    ])

def cancel_kb(lang, skip=False):
    t = T[lang]
    rows = [[KeyboardButton(text=t["btn_skip"], style="primary")]] if skip else []
    rows.append([KeyboardButton(text=t["btn_cancel"], style="danger")])
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=rows)

def lang_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang:uz", style="success"),
         InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang:ru", style="primary")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang:en", style="primary"),
         InlineKeyboardButton(text="🇨🇳 中文", callback_data="lang:zh", style="success")],
    ])

def fuel_kb(lang):
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["fuel_ice"], callback_data="fuel:ice", style="primary")],
        [InlineKeyboardButton(text=t["fuel_hybrid"], callback_data="fuel:hybrid", style="success")],
        [InlineKeyboardButton(text=t["fuel_serial"], callback_data="fuel:serial", style="success")],
        [InlineKeyboardButton(text=t["fuel_ev"], callback_data="fuel:ev", style="primary")],
    ])


class Calc(StatesGroup):
    fuel = State()
    year = State()
    cc = State()
    price = State()
    delivery = State()


def fmt(n: float) -> str:
    return f"{n:,.0f}".replace(",", " ")

def btn_texts(key):
    return {T[l][key] for l in T}


# Logistika va valyuta kursi alohida modullarda; ularni asosiy menyu tugmalari ochadi
logistics_router, logistics_start = logistics.build_router(get_lang, main_kb, cancel_kb)
currency_router, currency_start = currency.build_router(get_lang, main_kb, cancel_kb)
cert_router, cert_start = certificate.build_router(get_lang, main_kb, cancel_kb)
trade_router, trade_start = trade.build_router(get_lang, main_kb, cancel_kb)


# ---------- Logotip: salomlashuv xabari logotip bilan chiqadi ----------
LOGO_FILE = Path(__file__).with_name("logo.jpg")
_logo_id = None  # birinchi yuborilgandan keyin Telegram file_id qayta ishlatiladi

async def send_welcome(m: Message, lang: str):
    global _logo_id
    if LOGO_FILE.exists():
        try:
            sent = await m.answer_photo(_logo_id or FSInputFile(LOGO_FILE),
                                        caption=T[lang]["welcome"], reply_markup=main_kb(lang))
            _logo_id = sent.photo[-1].file_id
            return
        except Exception as e:
            logging.error("Logotipni yuborib bo'lmadi: %r", e)
    await m.answer(T[lang]["welcome"], reply_markup=main_kb(lang))


# ---------- Handlerlar ----------
@dp.message(CommandStart())
async def start(m: Message, state: FSMContext):
    await state.clear()
    if str(m.from_user.id) not in USERS:
        await m.answer(T["uz"]["choose_lang"], reply_markup=lang_kb())
    else:
        await send_welcome(m, get_lang(m.from_user.id))

@dp.message(Command("lang"))
@dp.message(F.text.in_(btn_texts("btn_lang")))
async def change_lang(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(T["uz"]["choose_lang"], reply_markup=lang_kb())

@dp.callback_query(F.data.startswith("lang:"))
async def lang_chosen(c: CallbackQuery):
    lang = c.data.split(":")[1]
    if lang not in T:
        return await c.answer()
    await set_lang(c.from_user, lang)
    await c.message.delete()
    await send_welcome(c.message, lang)
    await c.answer()

@dp.message(F.text.in_(btn_texts("btn_info")))
async def info(m: Message):
    lang = get_lang(m.from_user.id)
    await m.answer(T[lang]["info"].format(brv=fmt(R.BRV), max=R.MAX_AGE_ICE))

@dp.message(Command("support"))
@dp.message(F.text.in_(btn_texts("btn_support")))
async def support(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    await state.clear()
    admins = "\n".join(f"👤 @{u}" for u in SUPPORT_USERNAMES)
    await m.answer(T[lang]["support"].format(admins=admins, phone=SUPPORT_PHONE),
                   reply_markup=support_kb(lang))

@dp.message(Command("logistika"))
@dp.message(F.text.in_(btn_texts("btn_logistics")))
async def logistics_menu(m: Message, state: FSMContext):
    await logistics_start(m, state)

@dp.message(F.text.in_(btn_texts("btn_currency")))
async def currency_menu(m: Message, state: FSMContext):
    await currency_start(m, state)

@dp.message(F.text.in_(btn_texts("btn_cert")))
async def cert_menu(m: Message, state: FSMContext):
    await cert_start(m, state)

@dp.message(Command("zakaz"))
@dp.message(F.text.in_(btn_texts("btn_trade")))
async def trade_menu(m: Message, state: FSMContext):
    await trade_start(m, state)

@dp.message(Command("setlogo"))
async def set_logo(m: Message):
    """Admin: botning profil rasmini logo.jpg ga almashtiradi."""
    if not admin.is_admin(m):
        return
    from aiogram.types import InputProfilePhotoStatic
    try:
        await m.bot.set_my_profile_photo(photo=InputProfilePhotoStatic(photo=FSInputFile(LOGO_FILE)))
        await m.answer("✅ Bot profil rasmi logotipga almashtirildi.")
    except Exception as e:
        await m.answer(f"⚠️ Profil rasmini o'rnatib bo'lmadi: {e}\n"
                       "@BotFather → /setuserpic orqali qo'lda o'rnating.")

@dp.message(F.text.in_(btn_texts("btn_cancel")))
async def cancel(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    await state.clear()
    await m.answer(T[lang]["cancelled"], reply_markup=main_kb(lang))

@dp.message(Command("calc"))
@dp.message(F.text.in_(btn_texts("btn_calc")))
async def calc_start(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    await state.clear()
    await state.set_state(Calc.fuel)
    await m.answer("🚗", reply_markup=cancel_kb(lang))
    await m.answer(T[lang]["ask_fuel"], reply_markup=fuel_kb(lang))

@dp.callback_query(Calc.fuel, F.data.startswith("fuel:"))
async def fuel_chosen(c: CallbackQuery, state: FSMContext):
    lang = get_lang(c.from_user.id)
    fuel = c.data.split(":")[1]
    await state.update_data(fuel=fuel)
    await c.message.edit_text(f"✅ {T[lang]['fuel_' + fuel]}")
    await state.set_state(Calc.year)
    await c.message.answer(T[lang]["ask_year"])
    await c.answer()

@dp.message(Calc.year)
async def year_in(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    try:
        year = int(m.text.strip())
        assert 1950 <= year <= dt.date.today().year + 1
    except Exception:
        return await m.answer(T[lang]["bad_year"])
    await state.update_data(year=year)
    data = await state.get_data()
    if data["fuel"] == "ev":
        await state.update_data(cc=0)
        await state.set_state(Calc.price)
        return await m.answer(T[lang]["ask_price"])
    await state.set_state(Calc.cc)
    await m.answer(T[lang]["ask_cc"])

@dp.message(Calc.cc)
async def cc_in(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    try:
        cc = int(m.text.strip().replace(" ", ""))
        assert 500 <= cc <= 10000
    except Exception:
        return await m.answer(T[lang]["bad_cc"])
    await state.update_data(cc=cc)
    await state.set_state(Calc.price)
    await m.answer(T[lang]["ask_price"])

def parse_num(text: str) -> float:
    n = float(text.strip().replace(" ", "").replace(",", ".").replace("$", ""))
    assert n >= 0
    return n

@dp.message(Calc.price)
async def price_in(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    try:
        price = parse_num(m.text)
        assert price > 0
    except Exception:
        return await m.answer(T[lang]["bad_num"])
    await state.update_data(price=price)
    await state.set_state(Calc.delivery)
    await m.answer(T[lang]["ask_delivery"], reply_markup=cancel_kb(lang, skip=True))

@dp.message(Calc.delivery)
async def delivery_in(m: Message, state: FSMContext):
    lang = get_lang(m.from_user.id)
    t = T[lang]
    if m.text in btn_texts("btn_skip"):
        delivery = 0.0
    else:
        try:
            delivery = parse_num(m.text)
        except Exception:
            return await m.answer(t["bad_num"])

    d = await state.get_data()
    await state.clear()
    rate = await usd_rate()
    r = calculate(d["fuel"], d["year"], d["cc"], d["price"], delivery, rate)

    text = t["too_old"].format(max=R.MAX_AGE_ICE, age=r.age) if r.too_old else ""
    text += t["result"].format(
        fuel=t["fuel_" + d["fuel"]], year=d["year"], age=max(r.age, 0),
        cc_line=t["cc_line"].format(cc=fmt(d["cc"])) if d["cc"] else "",
        price=fmt(d["price"]), delivery=fmt(delivery), value=fmt(r.customs_value),
        rate=f"{rate:,.2f}".replace(",", " "),
        duty=fmt(r.duty), vat=fmt(r.vat),
        util_brv=f"{r.util_brv:g}", util=fmt(r.util_uzs), clear=fmt(r.clearance_uzs),
        total=fmt(r.total_uzs), total_usd=fmt(r.total_usd),
        grand=fmt(r.customs_value + r.total_usd),
    )
    await m.answer(text, reply_markup=main_kb(lang))
    try:
        await db.add_calc(m.from_user, d["fuel"], d["year"], d["cc"], d["price"], delivery,
                          r.total_uzs, r.total_usd)
    except Exception as e:
        logging.error("Hisob-kitobni bazaga yozib bo'lmadi: %r", e)


dp.include_router(logistics_router)
dp.include_router(currency_router)
dp.include_router(cert_router)
dp.include_router(trade_router)
dp.include_router(admin.build_router())


async def run_webhook(bot: Bot, base_url: str):
    """Serverda (Render) ishlash: Telegram xabarlarni webhook orqali yuboradi."""
    from aiohttp import web
    from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

    path = "/webhook"
    secret = TOKEN.split(":")[1][:32].replace("-", "x")
    app = web.Application()
    app.router.add_get("/", lambda r: web.Response(text="Bot ishlayapti"))
    SimpleRequestHandler(dispatcher=dp, bot=bot, secret_token=secret).register(app, path=path)
    setup_application(app, dp, bot=bot)

    async def on_startup(_):
        await bot.set_webhook(base_url.rstrip("/") + path, secret_token=secret,
                              drop_pending_updates=False)
    app.on_startup.append(on_startup)

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    await web.TCPSite(runner, "0.0.0.0", port).start()
    print(f"✅ Webhook rejimida ishga tushdi: {base_url} (port {port})")
    await asyncio.Event().wait()


async def main():
    if not TOKEN:
        raise SystemExit("BOT_TOKEN topilmadi! token.txt fayliga tokeningizni yozing.")
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    # /start dan oldin ko'rinadigan bot tavsifi (eski "Avto Kalkulyator" matni o'rniga)
    # Telegram ilovasi tiliga qarab ko'rsatiladi; boshqa tillarda — o'zbekcha (standart)
    for code, lang in ((None, "uz"), ("ru", "ru"), ("en", "en"), ("zh", "zh")):
        try:
            await bot.set_my_description(T[lang]["bot_description"], language_code=code)
            await bot.set_my_short_description(T[lang]["bot_short_description"], language_code=code)
        except Exception as e:
            print(f"Bot tavsifini o'rnatib bo'lmadi ({lang}):", e)
    await db.init()
    USERS.update(await db.user_langs())
    await admin.set_admin_commands(bot)
    await currency.load_manual(bot)  # admin /setkurs bilan kiritgan CBU kursi
    base_url = os.getenv("WEBHOOK_URL") or os.getenv("RENDER_EXTERNAL_URL")
    if base_url:
        await run_webhook(bot, base_url)
    else:
        await bot.delete_webhook(drop_pending_updates=False)
        print("✅ Bot ishga tushdi. To'xtatish uchun Ctrl+C bosing.")
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
