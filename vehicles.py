"""Fura, tyagach va prisep: naqd yoki bank kartasi orqali xarid so'rovnomasi.

Mijoz qanday texnika kerakligini va qulay xarid shartlarini tanlaydi,
telefon raqamini qoldiradi; ariza bazaga yoziladi va adminga yuboriladi.
"""
import logging
from html import escape

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import db
from logistics import admin_ids, phone_kb, PHONE_RE
from texts import T

# Tugmali savollar: maydon -> variantlar (matnlari texts.py da "vh_<maydon>")
OPTIONS = {
    "type": ("fura", "tractor", "trailer"),
    "trailer": ("tent", "ref", "platform", "dump", "tank", "other"),
    "condition": ("new", "used", "any"),
    "count": ("c1", "c2", "c4", "c10"),
    "pay": ("cash", "card"),
}
FIELDS = ("type", "trailer", "condition", "count", "pay", "region", "name", "phone")


class Veh(StatesGroup):
    type = State()
    trailer = State()
    condition = State()
    count = State()
    pay = State()
    region = State()
    name = State()
    phone = State()
    confirm = State()


def next_field(d: dict, field: str) -> str:
    """Keyingi savol: prisep turi faqat prisep yoki fura tanlanganda so'raladi."""
    i = FIELDS.index(field) + 1
    while True:
        f = FIELDS[i]
        if f == "trailer" and d.get("type") == "tractor":
            i += 1
        else:
            return f


# ---------- Klaviaturalar ----------
def options_kb(lang, field):
    labels = T[lang]["vh_" + field]
    buttons = [InlineKeyboardButton(text=labels[k], callback_data=f"vh:{field}:{k}")
               for k in OPTIONS[field]]
    per_row = 1 if field in ("type", "pay") else 2
    return InlineKeyboardMarkup(inline_keyboard=[buttons[i:i + per_row]
                                                 for i in range(0, len(buttons), per_row)])

def confirm_kb(lang):
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["lg_btn_confirm"], callback_data="vh:confirm")],
        [InlineKeyboardButton(text=t["lg_btn_drop"], callback_data="vh:drop")],
    ])


# ---------- Yordamchilar ----------
def value_text(lang, d: dict, field: str) -> str | None:
    if field in OPTIONS:
        return T[lang]["vh_" + field].get(d.get(field)) if d.get(field) else None
    return escape(d[field]) if d.get(field) else None

def summary(lang, d: dict) -> str:
    labels = T[lang]["vh_field"]
    lines = []
    for f in FIELDS:
        v = value_text(lang, d, f)
        if v:
            lines.append(f"<b>{labels[f]}:</b> {v}")
    return "\n".join(lines)


def build_router(get_lang, main_kb, cancel_kb):
    """(router, start) qaytaradi: start — asosiy menyudagi tugma uchun."""
    router = Router(name="vehicles")

    async def ask(m: Message, state: FSMContext, field: str, lang: str):
        await state.set_state(getattr(Veh, field))
        t = T[lang]
        if field in OPTIONS:
            await m.answer(t["vh_ask_" + field], reply_markup=options_kb(lang, field))
        elif field == "phone":
            await m.answer(t["tr_ask_phone"], reply_markup=phone_kb(lang))
        else:
            await m.answer(t["vh_ask_" + field], reply_markup=cancel_kb(lang))

    async def vehicles_start(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await state.clear()
        await m.answer(T[lang]["vh_intro"], reply_markup=cancel_kb(lang))
        await ask(m, state, "type", lang)

    # ----- Tugmali savollar -----
    @router.callback_query(F.data.regexp(r"^vh:[a-z]+:[a-z0-9]+$"))
    async def option_chosen(c: CallbackQuery, state: FSMContext):
        _, field, key = c.data.split(":")
        current = await state.get_state()
        if field not in OPTIONS or key not in OPTIONS[field] or current != getattr(Veh, field).state:
            return await c.answer()
        lang = get_lang(c.from_user.id)
        t = T[lang]
        await state.update_data(**{field: key})
        if field == "type" and key == "tractor":
            await state.update_data(trailer=None)
        await c.message.edit_text(f"{t['vh_field'][field]}: ✅ {t['vh_' + field][key]}")
        await c.answer()
        await ask(c.message, state, next_field(await state.get_data(), field), lang)

    @router.message(Veh.type)
    @router.message(Veh.trailer)
    @router.message(Veh.condition)
    @router.message(Veh.count)
    @router.message(Veh.pay)
    @router.message(Veh.confirm)
    async def use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    # ----- Matnli savollar -----
    async def text_in(m: Message, state: FSMContext, field: str):
        lang = get_lang(m.from_user.id)
        if not m.text or len(m.text.strip()) < 2:
            return await m.answer(T[lang]["ct_bad_text"])
        await state.update_data(**{field: m.text.strip()[:200]})
        await ask(m, state, next_field(await state.get_data(), field), lang)

    @router.message(Veh.region)
    async def region_in(m: Message, state: FSMContext):
        await text_in(m, state, "region")

    @router.message(Veh.name)
    async def name_in(m: Message, state: FSMContext):
        await text_in(m, state, "name")

    # ----- Telefon (majburiy) -----
    @router.message(Veh.phone)
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
        await state.set_state(Veh.confirm)
        await m.answer("👇", reply_markup=cancel_kb(lang))
        await m.answer(T[lang]["vh_confirm"].format(summary=summary(lang, await state.get_data())),
                       reply_markup=confirm_kb(lang))

    # ----- Tasdiqlash -----
    @router.callback_query(Veh.confirm, F.data == "vh:drop")
    async def drop(c: CallbackQuery, state: FSMContext):
        lang = get_lang(c.from_user.id)
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.message.answer(T[lang]["cancelled"], reply_markup=main_kb(lang))
        await c.answer()

    @router.callback_query(Veh.confirm, F.data == "vh:confirm")
    async def confirm(c: CallbackQuery, state: FSMContext, bot: Bot):
        lang = get_lang(c.from_user.id)
        d = await state.get_data()
        if not d.get("phone"):
            await c.answer()
            return await ask(c.message, state, "phone", lang)
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.answer()

        user = c.from_user
        no = await db.add_vehicle(user, {"lang": lang, **{f: d.get(f) for f in FIELDS}})
        await c.message.answer(T[lang]["vh_thanks"].format(no=no), reply_markup=main_kb(lang))

        who = f'<a href="tg://user?id={user.id}">{escape(user.full_name)}</a>'
        if user.username:
            who += f" (@{escape(user.username)})"
        text = T["uz"]["vh_admin"].format(no=no, who=who, summary=summary("uz", d))
        admins = admin_ids()
        if not admins:
            logging.warning("ADMIN_ID o'rnatilmagan: texnika arizasi #%s faqat bazaga yozildi", no)
        for admin in admins:
            try:
                await bot.send_message(admin, text)
            except Exception as e:
                logging.error("Texnika arizasi #%s adminga (%s) yuborilmadi: %s", no, admin, e)

    return router, vehicles_start
