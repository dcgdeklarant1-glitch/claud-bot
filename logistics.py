"""Logistika xizmati: yuk tashishga buyurtma (bosqichma-bosqich, tugmali forma)."""
import logging
import os
import re
from html import escape

from aiogram import Bot, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

import db
from texts import T

PHONE_RE = re.compile(r"^\+?\d[\d\s\-()]{6,18}\d$")

CARGO = ("furniture", "food", "building", "appliances", "textile", "other")
WEIGHT = ("w1", "w2", "w3", "w4", "w5", "w6", "w7")
VOLUME = ("v1", "v2", "v3", "v4", "v5", "v6", "unknown")
READY = ("now", "today", "tomorrow", "days", "other")
FIELDS = ("origin", "destination", "cargo", "weight", "volume", "ready", "phone")


class Logi(StatesGroup):
    origin = State()
    destination = State()
    cargo = State()
    cargo_other = State()
    weight = State()
    volume = State()
    ready = State()
    ready_other = State()
    phone = State()
    confirm = State()


# ---------- Klaviaturalar ----------
def location_kb(lang):
    t = T[lang]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=t["lg_btn_location"], request_location=True)],
        [KeyboardButton(text=t["btn_cancel"])],
    ])

def phone_kb(lang):
    t = T[lang]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=t["lg_btn_phone"], request_contact=True)],
        [KeyboardButton(text=t["btn_cancel"])],
    ])

def options_kb(lang, field, keys, per_row=2):
    labels = T[lang]["lg_" + field]
    buttons = [InlineKeyboardButton(text=labels[k], callback_data=f"lg:{field}:{k}") for k in keys]
    return InlineKeyboardMarkup(inline_keyboard=[buttons[i:i + per_row]
                                                 for i in range(0, len(buttons), per_row)])

def confirm_kb(lang):
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["lg_btn_confirm"], callback_data="lg:confirm")],
        [InlineKeyboardButton(text=t["lg_btn_edit"], callback_data="lg:edit"),
         InlineKeyboardButton(text=t["lg_btn_drop"], callback_data="lg:drop")],
    ])

def edit_kb(lang):
    t = T[lang]
    labels = t["lg_field"]
    buttons = [InlineKeyboardButton(text=labels[f], callback_data=f"lg:edit:{f}") for f in FIELDS]
    rows = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
    rows.append([InlineKeyboardButton(text=t["lg_btn_back"], callback_data="lg:back")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


# ---------- Yordamchilar ----------
def place_text(place: dict) -> str:
    if "lat" in place:
        return (f'📍 <a href="https://maps.google.com/?q={place["lat"]},{place["lon"]}">'
                f'{place["lat"]:.5f}, {place["lon"]:.5f}</a>')
    return escape(place["text"])

def value_text(lang, d: dict, field: str) -> str:
    t = T[lang]
    if field in ("origin", "destination"):
        return place_text(d[field])
    if field == "phone":
        return escape(d["phone"])
    if d.get(field + "_text"):
        return escape(d[field + "_text"])
    return t["lg_" + field][d[field]]

def summary(lang, d: dict) -> str:
    labels = T[lang]["lg_field"]
    return "\n".join(f"<b>{labels[f]}:</b> {value_text(lang, d, f)}" for f in FIELDS)

def admin_ids() -> list:
    """Buyurtmalar shu Telegram ID larga yuboriladi (vergul bilan bir nechta: ADMIN_ID=111,222)."""
    return [int(x) for x in re.split(r"[,\s]+", os.getenv("ADMIN_ID", "")) if x.isdigit()]


def build_router(get_lang, main_kb, cancel_kb):
    """(router, start) qaytaradi: start — asosiy menyudagi «Logistika» tugmasi uchun."""
    router = Router(name="logistics")

    async def ask(m: Message, state: FSMContext, field: str):
        """Maydon uchun savol beradi va kerakli holatga o'tadi."""
        lang = get_lang(m.chat.id)
        t = T[lang]
        if field in ("origin", "destination"):
            await state.set_state(getattr(Logi, field))
            await m.answer(t["lg_ask_" + field], reply_markup=location_kb(lang))
        elif field == "phone":
            await state.set_state(Logi.phone)
            await m.answer(t["lg_ask_phone"], reply_markup=phone_kb(lang))
        else:
            keys = {"cargo": CARGO, "weight": WEIGHT, "volume": VOLUME, "ready": READY}[field]
            await state.set_state(getattr(Logi, field))
            await m.answer("👇", reply_markup=cancel_kb(lang))
            await m.answer(t["lg_ask_" + field], reply_markup=options_kb(lang, field, keys))

    async def show_confirm(m: Message, state: FSMContext):
        lang = get_lang(m.chat.id)
        t = T[lang]
        await state.update_data(editing=False)
        await state.set_state(Logi.confirm)
        await m.answer("👇", reply_markup=cancel_kb(lang))
        await m.answer(t["lg_confirm"].format(summary=summary(lang, await state.get_data())),
                       reply_markup=confirm_kb(lang), disable_web_page_preview=True)

    async def done(m: Message, state: FSMContext, field: str):
        """Maydon to'ldirildi: tahrirlashda tasdiqlashga, aks holda keyingi savolga o'tadi."""
        data = await state.get_data()
        if data.get("editing") or field == FIELDS[-1]:
            return await show_confirm(m, state)
        await ask(m, state, FIELDS[FIELDS.index(field) + 1])

    # ----- Asosiy menyudan logistika tanlandi -----
    async def logistics_start(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await state.clear()
        await m.answer(T[lang]["lg_intro"])
        await ask(m, state, "origin")

    # ----- Qayerdan / qayerga -----
    async def place_in(m: Message, state: FSMContext, field: str):
        lang = get_lang(m.from_user.id)
        if m.location:
            place = {"lat": m.location.latitude, "lon": m.location.longitude}
        elif m.text and len(m.text.strip()) >= 2:
            place = {"text": m.text.strip()[:200]}
        else:
            return await m.answer(T[lang]["lg_bad_place"])
        await state.update_data(**{field: place})
        await done(m, state, field)

    @router.message(Logi.origin)
    async def origin_in(m: Message, state: FSMContext):
        await place_in(m, state, "origin")

    @router.message(Logi.destination)
    async def destination_in(m: Message, state: FSMContext):
        await place_in(m, state, "destination")

    # ----- Tugmali tanlovlar: yuk turi, og'irligi, hajmi, tayyor vaqti -----
    @router.callback_query(F.data.regexp(r"^lg:(cargo|weight|volume|ready):\w+$"))
    async def option_chosen(c: CallbackQuery, state: FSMContext):
        _, field, key = c.data.split(":")
        current = await state.get_state()
        if current != getattr(Logi, field).state:
            return await c.answer()  # eski xabardagi tugma
        lang = get_lang(c.from_user.id)
        t = T[lang]
        await c.message.edit_text(f"{t['lg_field'][field]}: ✅ {t['lg_' + field][key]}")
        await c.answer()
        if key == "other":
            await state.update_data(**{field: key})
            await state.set_state(getattr(Logi, field + "_other"))
            return await c.message.answer(t["lg_ask_" + field + "_other"])
        await state.update_data(**{field: key, field + "_text": None})
        await done(c.message, state, field)

    async def other_in(m: Message, state: FSMContext, field: str):
        lang = get_lang(m.from_user.id)
        if not m.text or len(m.text.strip()) < 2:
            return await m.answer(T[lang]["lg_ask_" + field + "_other"])
        await state.update_data(**{field + "_text": m.text.strip()[:200]})
        await done(m, state, field)

    @router.message(Logi.cargo_other)
    async def cargo_other_in(m: Message, state: FSMContext):
        await other_in(m, state, "cargo")

    @router.message(Logi.ready_other)
    async def ready_other_in(m: Message, state: FSMContext):
        await other_in(m, state, "ready")

    @router.message(StateFilter(Logi.cargo, Logi.weight, Logi.volume, Logi.ready))
    async def use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    # ----- Telefon -----
    @router.message(Logi.phone)
    async def phone_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        if m.contact:
            phone = m.contact.phone_number
            phone = phone if phone.startswith("+") else "+" + phone
        elif m.text and PHONE_RE.match(m.text.strip()):
            phone = m.text.strip()
        else:
            return await m.answer(T[lang]["lg_bad_phone"], reply_markup=phone_kb(lang))
        await state.update_data(phone=phone)
        await done(m, state, "phone")

    # ----- Tasdiqlash / tahrirlash -----
    @router.callback_query(Logi.confirm, F.data == "lg:edit")
    async def edit_menu(c: CallbackQuery):
        lang = get_lang(c.from_user.id)
        await c.message.edit_reply_markup(reply_markup=edit_kb(lang))
        await c.answer(T[lang]["lg_edit_which"])

    @router.callback_query(Logi.confirm, F.data == "lg:back")
    async def edit_back(c: CallbackQuery):
        await c.message.edit_reply_markup(reply_markup=confirm_kb(get_lang(c.from_user.id)))
        await c.answer()

    @router.callback_query(Logi.confirm, F.data.startswith("lg:edit:"))
    async def edit_field(c: CallbackQuery, state: FSMContext):
        field = c.data.split(":")[2]
        if field not in FIELDS:
            return await c.answer()
        await c.message.edit_reply_markup(reply_markup=None)
        await state.update_data(editing=True)
        await c.answer()
        await ask(c.message, state, field)

    @router.callback_query(Logi.confirm, F.data == "lg:drop")
    async def drop(c: CallbackQuery, state: FSMContext):
        lang = get_lang(c.from_user.id)
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.message.answer(T[lang]["cancelled"], reply_markup=main_kb(lang))
        await c.answer()

    @router.callback_query(Logi.confirm, F.data == "lg:confirm")
    async def confirm(c: CallbackQuery, state: FSMContext, bot: Bot):
        lang = get_lang(c.from_user.id)
        d = await state.get_data()
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.answer()

        user = c.from_user
        no = await db.add_order(user, {"lang": lang, **{f: d[f] for f in FIELDS},
                                       "cargo_text": d.get("cargo_text"), "ready_text": d.get("ready_text")})

        await c.message.answer(T[lang]["lg_thanks"].format(no=no), reply_markup=main_kb(lang))

        who = f'<a href="tg://user?id={user.id}">{escape(user.full_name)}</a>'
        if user.username:
            who += f" (@{escape(user.username)})"
        text = T["uz"]["lg_admin"].format(no=no, who=who, summary=summary("uz", d))
        admins = admin_ids()
        if not admins:
            logging.warning("ADMIN_ID o'rnatilmagan: #%s buyurtma faqat bazaga yozildi", no)
        for admin in admins:
            try:
                await bot.send_message(admin, text, disable_web_page_preview=True)
            except Exception as e:
                logging.error("Buyurtma #%s adminga (%s) yuborilmadi: %s", no, admin, e)

    @router.message(Logi.confirm)
    async def confirm_use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    return router, logistics_start
