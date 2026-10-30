"""Import / eksport: mijoz zakaz qoldiradi (telefon raqami majburiy), menejer bog'lanadi."""
import logging
from html import escape

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import db
from logistics import admin_ids, phone_kb, PHONE_RE
from texts import T

DIRECTION = ("import", "export")
FIELDS = ("direction", "product", "country", "volume", "name", "phone")


class Trade(StatesGroup):
    direction = State()
    product = State()
    country = State()
    volume = State()
    name = State()
    phone = State()
    confirm = State()


# ---------- Klaviaturalar ----------
def direction_kb(lang):
    labels = T[lang]["tr_direction"]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=labels["import"], callback_data="tr:dir:import"),
         InlineKeyboardButton(text=labels["export"], callback_data="tr:dir:export")],
    ])

def confirm_kb(lang):
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["lg_btn_confirm"], callback_data="tr:confirm")],
        [InlineKeyboardButton(text=t["lg_btn_drop"], callback_data="tr:drop")],
    ])


# ---------- Yordamchilar ----------
def value_text(lang, d: dict, field: str) -> str:
    t = T[lang]
    if field == "direction":
        return t["tr_direction"][d["direction"]]
    return escape(d[field]) if d.get(field) else t["ct_none"]

def summary(lang, d: dict) -> str:
    labels = T[lang]["tr_field"]
    return "\n".join(f"<b>{labels[f]}:</b> {value_text(lang, d, f)}" for f in FIELDS)


def build_router(get_lang, main_kb, cancel_kb):
    """(router, start) qaytaradi: start — asosiy menyudagi «Import / Eksport» tugmasi uchun."""
    router = Router(name="trade")
    skip_texts = {T[l]["btn_skip"] for l in T}

    async def text_in(m: Message, state: FSMContext, field: str, next_state, question: str, kb):
        lang = get_lang(m.from_user.id)
        if not m.text or len(m.text.strip()) < 2:
            return await m.answer(T[lang]["ct_bad_text"])
        await state.update_data(**{field: m.text.strip()[:500]})
        await state.set_state(next_state)
        await m.answer(question, reply_markup=kb)

    # ----- Asosiy menyudan import/eksport tanlandi -----
    async def trade_start(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await state.clear()
        await state.set_state(Trade.direction)
        await m.answer(T[lang]["tr_intro"], reply_markup=cancel_kb(lang))
        await m.answer(T[lang]["tr_ask_direction"], reply_markup=direction_kb(lang))

    @router.callback_query(Trade.direction, F.data.startswith("tr:dir:"))
    async def direction_chosen(c: CallbackQuery, state: FSMContext):
        key = c.data.split(":")[2]
        if key not in DIRECTION:
            return await c.answer()
        lang = get_lang(c.from_user.id)
        t = T[lang]
        await state.update_data(direction=key)
        await c.message.edit_text(f"{t['tr_field']['direction']}: ✅ {t['tr_direction'][key]}")
        await c.answer()
        await state.set_state(Trade.product)
        await c.message.answer(t["tr_ask_product"], reply_markup=cancel_kb(lang))

    @router.message(Trade.direction)
    async def direction_use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    @router.message(Trade.product)
    async def product_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        d = await state.get_data()
        await text_in(m, state, "product", Trade.country,
                      T[lang]["tr_ask_country_" + d["direction"]], cancel_kb(lang))

    @router.message(Trade.country)
    async def country_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await text_in(m, state, "country", Trade.volume, T[lang]["tr_ask_volume"], cancel_kb(lang, skip=True))

    @router.message(Trade.volume)
    async def volume_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        if m.text and m.text in skip_texts:
            await state.update_data(volume=None)
            await state.set_state(Trade.name)
            return await m.answer(T[lang]["tr_ask_name"], reply_markup=cancel_kb(lang))
        await text_in(m, state, "volume", Trade.name, T[lang]["tr_ask_name"], cancel_kb(lang))

    @router.message(Trade.name)
    async def name_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await text_in(m, state, "name", Trade.phone, T[lang]["tr_ask_phone"], phone_kb(lang))

    # ----- Telefon (majburiy: o'tkazib yuborib bo'lmaydi) -----
    @router.message(Trade.phone)
    async def phone_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        if m.contact:
            phone = m.contact.phone_number
            phone = phone if phone.startswith("+") else "+" + phone
        elif m.text and PHONE_RE.match(m.text.strip()):
            phone = m.text.strip()
        else:
            return await m.answer(T[lang]["tr_bad_phone"], reply_markup=phone_kb(lang))
        await state.update_data(phone=phone)
        await state.set_state(Trade.confirm)
        await m.answer("👇", reply_markup=cancel_kb(lang))
        await m.answer(T[lang]["tr_confirm"].format(summary=summary(lang, await state.get_data())),
                       reply_markup=confirm_kb(lang))

    # ----- Tasdiqlash -----
    @router.callback_query(Trade.confirm, F.data == "tr:drop")
    async def drop(c: CallbackQuery, state: FSMContext):
        lang = get_lang(c.from_user.id)
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.message.answer(T[lang]["cancelled"], reply_markup=main_kb(lang))
        await c.answer()

    @router.callback_query(Trade.confirm, F.data == "tr:confirm")
    async def confirm(c: CallbackQuery, state: FSMContext, bot: Bot):
        lang = get_lang(c.from_user.id)
        d = await state.get_data()
        if not d.get("phone"):  # telefonsiz zakaz qabul qilinmaydi
            await state.set_state(Trade.phone)
            await c.answer()
            return await c.message.answer(T[lang]["tr_ask_phone"], reply_markup=phone_kb(lang))
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.answer()

        user = c.from_user
        no = await db.add_trade(user, {"lang": lang, **{f: d.get(f) for f in FIELDS}})

        await c.message.answer(T[lang]["tr_thanks"].format(no=no), reply_markup=main_kb(lang))

        who = f'<a href="tg://user?id={user.id}">{escape(user.full_name)}</a>'
        if user.username:
            who += f" (@{escape(user.username)})"
        text = T["uz"]["tr_admin"].format(no=no, who=who, summary=summary("uz", d))
        admins = admin_ids()
        if not admins:
            logging.warning("ADMIN_ID o'rnatilmagan: import/eksport zakazi #%s faqat bazaga yozildi", no)
        for admin in admins:
            try:
                await bot.send_message(admin, text)
            except Exception as e:
                logging.error("Import/eksport zakazi #%s adminga (%s) yuborilmadi: %s", no, admin, e)

    @router.message(Trade.confirm)
    async def confirm_use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    return router, trade_start
