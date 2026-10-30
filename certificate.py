"""Sertifikat kerakligini aniqlash: mijoz tovar ma'lumotlarini yuboradi, mutaxassis javob beradi."""
import logging
from html import escape

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import db
from logistics import admin_ids, phone_kb, PHONE_RE
from texts import T

PURPOSE = ("sale", "personal")
FIELDS = ("product", "code", "country", "purpose", "file", "phone")


class Cert(StatesGroup):
    product = State()
    code = State()
    country = State()
    purpose = State()
    file = State()
    phone = State()
    confirm = State()


class CertReply(StatesGroup):
    """Mutaxassis (admin) mijozga javob yozmoqda."""
    text = State()


# ---------- Klaviaturalar ----------
def purpose_kb(lang):
    labels = T[lang]["ct_purpose"]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=labels[k], callback_data=f"ct:purpose:{k}") for k in PURPOSE]
    ])

def confirm_kb(lang):
    t = T[lang]
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t["lg_btn_confirm"], callback_data="ct:confirm")],
        [InlineKeyboardButton(text=t["lg_btn_drop"], callback_data="ct:drop")],
    ])

def reply_kb(user_id: int, no: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=T["uz"]["ct_btn_reply"], callback_data=f"ct:reply:{user_id}:{no}")]
    ])


# ---------- Yordamchilar ----------
def value_text(lang, d: dict, field: str) -> str:
    t = T[lang]
    if field == "purpose":
        return t["ct_purpose"][d["purpose"]]
    if field == "file":
        return t["ct_file_yes"] if d.get("file") else t["ct_none"]
    return escape(d[field]) if d.get(field) else t["ct_none"]

def summary(lang, d: dict) -> str:
    labels = T[lang]["ct_field"]
    return "\n".join(f"<b>{labels[f]}:</b> {value_text(lang, d, f)}" for f in FIELDS)


def build_router(get_lang, main_kb, cancel_kb):
    """(router, start) qaytaradi: start — asosiy menyudagi «Sertifikat» tugmasi uchun."""
    router = Router(name="certificate")

    async def text_in(m: Message, state: FSMContext, field: str, next_state, question: str, kb):
        lang = get_lang(m.from_user.id)
        if not m.text or len(m.text.strip()) < 2:
            return await m.answer(T[lang]["ct_bad_text"])
        await state.update_data(**{field: m.text.strip()[:500]})
        await state.set_state(next_state)
        await m.answer(T[lang][question], reply_markup=kb)

    # ----- Asosiy menyudan sertifikat tanlandi -----
    async def cert_start(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await state.clear()
        await state.set_state(Cert.product)
        await m.answer(T[lang]["ct_intro"])
        await m.answer(T[lang]["ct_ask_product"], reply_markup=cancel_kb(lang))

    @router.message(Cert.product)
    async def product_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        await text_in(m, state, "product", Cert.code, "ct_ask_code", cancel_kb(lang, skip=True))

    @router.message(Cert.code)
    async def code_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        if m.text and m.text in {T[l]["btn_skip"] for l in T}:
            await state.update_data(code=None)
            await state.set_state(Cert.country)
            return await m.answer(T[lang]["ct_ask_country"], reply_markup=cancel_kb(lang))
        await text_in(m, state, "code", Cert.country, "ct_ask_country", cancel_kb(lang))

    @router.message(Cert.country)
    async def country_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        if not m.text or len(m.text.strip()) < 2:
            return await m.answer(T[lang]["ct_bad_text"])
        await state.update_data(country=m.text.strip()[:200])
        await state.set_state(Cert.purpose)
        await m.answer(T[lang]["ct_ask_purpose"], reply_markup=purpose_kb(lang))

    # ----- Maqsad: sotish / shaxsiy -----
    @router.callback_query(Cert.purpose, F.data.startswith("ct:purpose:"))
    async def purpose_chosen(c: CallbackQuery, state: FSMContext):
        key = c.data.split(":")[2]
        if key not in PURPOSE:
            return await c.answer()
        lang = get_lang(c.from_user.id)
        t = T[lang]
        await state.update_data(purpose=key)
        await c.message.edit_text(f"{t['ct_field']['purpose']}: ✅ {t['ct_purpose'][key]}")
        await c.answer()
        await state.set_state(Cert.file)
        await c.message.answer(t["ct_ask_file"], reply_markup=cancel_kb(lang, skip=True))

    @router.message(Cert.purpose)
    async def purpose_use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    # ----- Rasm yoki hujjat (ixtiyoriy) -----
    @router.message(Cert.file)
    async def file_in(m: Message, state: FSMContext):
        lang = get_lang(m.from_user.id)
        if m.photo:
            await state.update_data(file={"type": "photo", "id": m.photo[-1].file_id})
        elif m.document:
            await state.update_data(file={"type": "document", "id": m.document.file_id})
        elif m.text and m.text in {T[l]["btn_skip"] for l in T}:
            await state.update_data(file=None)
        else:
            return await m.answer(T[lang]["ct_bad_file"])
        await state.set_state(Cert.phone)
        await m.answer(T[lang]["lg_ask_phone"], reply_markup=phone_kb(lang))

    # ----- Telefon -----
    @router.message(Cert.phone)
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
        await state.set_state(Cert.confirm)
        await m.answer("👇", reply_markup=cancel_kb(lang))
        await m.answer(T[lang]["ct_confirm"].format(summary=summary(lang, await state.get_data())),
                       reply_markup=confirm_kb(lang))

    # ----- Tasdiqlash -----
    @router.callback_query(Cert.confirm, F.data == "ct:drop")
    async def drop(c: CallbackQuery, state: FSMContext):
        lang = get_lang(c.from_user.id)
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.message.answer(T[lang]["cancelled"], reply_markup=main_kb(lang))
        await c.answer()

    @router.callback_query(Cert.confirm, F.data == "ct:confirm")
    async def confirm(c: CallbackQuery, state: FSMContext, bot: Bot):
        lang = get_lang(c.from_user.id)
        d = await state.get_data()
        await state.clear()
        await c.message.edit_reply_markup(reply_markup=None)
        await c.answer()

        user = c.from_user
        no = await db.add_cert(user, {"lang": lang, **{f: d.get(f) for f in FIELDS}})

        await c.message.answer(T[lang]["ct_thanks"].format(no=no), reply_markup=main_kb(lang))

        who = f'<a href="tg://user?id={user.id}">{escape(user.full_name)}</a>'
        if user.username:
            who += f" (@{escape(user.username)})"
        text = T["uz"]["ct_admin"].format(no=no, who=who, summary=summary("uz", d))
        admins = admin_ids()
        if not admins:
            logging.warning("ADMIN_ID o'rnatilmagan: sertifikat arizasi #%s faqat bazaga yozildi", no)
        for admin in admins:
            try:
                f = d.get("file")
                if f and f["type"] == "photo":
                    await bot.send_photo(admin, f["id"], caption=f"📎 #{no}")
                elif f:
                    await bot.send_document(admin, f["id"], caption=f"📎 #{no}")
                await bot.send_message(admin, text, reply_markup=reply_kb(user.id, no))
            except Exception as e:
                logging.error("Sertifikat arizasi #%s adminga (%s) yuborilmadi: %s", no, admin, e)

    @router.message(Cert.confirm)
    async def confirm_use_buttons(m: Message):
        await m.answer(T[get_lang(m.from_user.id)]["lg_use_buttons"])

    # ----- Mutaxassis javobi -----
    @router.callback_query(F.data.regexp(r"^ct:reply:\d+:\d+$"))
    async def reply_start(c: CallbackQuery, state: FSMContext):
        if c.from_user.id not in admin_ids():
            return await c.answer()
        _, _, user_id, no = c.data.split(":")
        await state.clear()
        await state.set_state(CertReply.text)
        await state.update_data(user_id=int(user_id), no=int(no))
        await c.answer()
        await c.message.answer(T["uz"]["ct_ask_reply"].format(no=no),
                               reply_markup=cancel_kb(get_lang(c.from_user.id)))

    @router.message(CertReply.text)
    async def reply_in(m: Message, state: FSMContext, bot: Bot):
        d = await state.get_data()
        await state.clear()
        user_id, no = d["user_id"], d["no"]
        header = T[get_lang(user_id)]["ct_answer"].format(no=no)
        try:
            if m.text:
                await bot.send_message(user_id, f"{header}\n\n{escape(m.text)}")
            else:
                await bot.send_message(user_id, header)
                await m.copy_to(user_id)
        except Exception as e:
            logging.error("Sertifikat javobi #%s mijozga (%s) yuborilmadi: %s", no, user_id, e)
            return await m.answer(T["uz"]["ct_reply_fail"].format(no=no),
                                  reply_markup=main_kb(get_lang(m.from_user.id)))
        await db.answer_cert(no, m.text or m.caption or "📎 (rasm / fayl)")
        await m.answer(T["uz"]["ct_reply_sent"].format(no=no),
                       reply_markup=main_kb(get_lang(m.from_user.id)))

    return router, cert_start
