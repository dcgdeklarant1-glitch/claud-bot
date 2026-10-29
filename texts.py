"""Bot matnlari: o'zbek (uz), rus (ru), ingliz (en) va xitoy (zh)."""

CHOOSE_LANG = "🌐 Tilni tanlang / Выберите язык / Choose language / 选择语言:"

T = {
    "uz": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "Assalomu alaykum! DCG Cargo botiga xush kelibsiz! 🚚\n\nLogistika, valyuta kursi va rastamojka hisob-kitobi.",
        "bot_short_description": "DCG Cargo rasmiy boti 🚚",
        "welcome": "👋 <b>ASSALOMU ALAYKUM!</b>\n\n🚚 <b>DCGCargo</b> botiga xush kelibsiz!\n\nQuyidagi tugmani bosing 👇",
        "btn_calc": "🚗 Rastamojkani hisoblash",
        "btn_info": "ℹ️ Ma'lumot",
        "btn_lang": "🌐 Tilni o'zgartirish",
        "btn_cancel": "❌ Bekor qilish",
        "btn_skip": "⏭ O'tkazib yuborish",
        "ask_fuel": "⛽️ Yoqilg'i turini tanlang:",
        "fuel_ice": "⛽️ Benzin / Dizel",
        "fuel_hybrid": "🔋 Gibrid",
        "fuel_serial": "🔌 Ketma-ket gibrid (EREV)",
        "fuel_ev": "⚡️ Elektro",
        "ask_year": "📅 Ishlab chiqarilgan yilini kiriting (masalan: <code>2023</code>):",
        "bad_year": "❗️ Yilni to'g'ri kiriting (masalan: 2022).",
        "ask_cc": "🔧 Dvigatel hajmini sm³ da kiriting (masalan: <code>1600</code>):",
        "bad_cc": "❗️ Dvigatel hajmini raqamda kiriting (500 – 10000).",
        "ask_price": "💵 Avtomobil narxini AQSh dollarida kiriting (masalan: <code>15000</code>):",
        "bad_num": "❗️ Raqam kiriting (masalan: 15000).",
        "ask_delivery": "🚚 Yetkazib berish narxi ($)? Bilmasangiz — «O'tkazib yuborish» ni bosing.",
        "cancelled": "Bekor qilindi.",
        "too_old": "⛔️ <b>Diqqat:</b> benzin/dizel avtomobillar {max} yildan eski bo'lsa, O'zbekistonga olib kirish taqiqlangan (avtomobil yoshi: {age} yil). Hisob faqat ma'lumot uchun.\n\n",
        "result": (
            "📊 <b>Hisob natijasi</b>\n\n"
            "⛽️ Yoqilg'i: {fuel}\n"
            "📅 Yili: {year} ({age} yil)\n"
            "{cc_line}"
            "💵 Narxi: ${price}\n"
            "🚚 Yetkazish: ${delivery}\n"
            "🧾 Bojxona qiymati: ${value}\n"
            "💱 Kurs: 1$ = {rate} so'm\n\n"
            "━━━━━━━━━━━━━━━\n"
            "🏛 Bojxona boji: ${duty}\n"
            "🧮 QQS (12%): ${vat}\n"
            "♻️ Utilizatsiya yig'imi: {util_brv} BHM = {util} so'm\n"
            "📑 Rasmiylashtiruv yig'imi: {clear} so'm\n"
            "━━━━━━━━━━━━━━━\n"
            "💰 <b>Jami rastamojka: {total} so'm</b>\n"
            "≈ <b>${total_usd}</b>\n\n"
            "🚘 <b>Avto + rastamojka ≈ ${grand}</b>\n\n"
            "⚠️ <i>Hisob taxminiy. Aniq summa bojxonada belgilanadi.</i>"
        ),
        "cc_line": "🔧 Dvigatel: {cc} sm³\n",
        "info": (
            "ℹ️ <b>Hisoblash qanday ishlaydi</b>\n\n"
            "• Bojxona boji: 1 yilgacha — 15% + $1/sm³; 1–3 yil — 30% + $2.5/sm³; 3 yildan katta — 40% + $3/sm³\n"
            "• Elektro va ketma-ket gibridlar bojdan ozod\n"
            "• QQS: 12% (qiymat + boj)\n"
            "• Utilizatsiya yig'imi: BHM da, dvigatel hajmi va yoshga qarab\n"
            "• 1 BHM = {brv} so'm\n"
            "• Benzin/dizel: {max} yildan eski, Euro-5 dan past va o'ng rulli avtolar taqiqlangan\n\n"
            "Kurs O'zbekiston Markaziy banki (cbu.uz) dan olinadi."
        ),
        # ---------- Logistika / valyuta / yordam ----------
        "btn_logistics": "🚚 Logistika",
        "btn_currency": "💱 Valyuta kursi",
        "btn_support": "🆘 Qo'llab-quvvatlash",
        "support": (
            "🆘 <b>Qo'llab-quvvatlash</b>\n\n"
            "Savollaringiz bo'lsa, administratorga murojaat qiling:\n\n"
            "{admins}\n"
            "📞 Telefon: {phone}"
        ),
        "support_btn_write": "✍️ Yozish:",
        # ---------- Valyuta kursi ----------
        "cur_title": "💱 <b>Valyuta kurslari</b> ({date})",
        "cur_sum": "so'm",
        "cur_source": "<i>Manba: O'zbekiston Markaziy banki (cbu.uz). ▲▼ — kechagi kunga nisbatan o'zgarish.</i>",
        "cur_btn_convert": "🧮 So'mga hisoblash",
        "cur_btn_refresh": "🔄 Yangilash",
        "cur_refreshed": "Kurslar yangilandi",
        "cur_pick": "🧮 Qaysi valyutani so'mga hisoblaymiz?",
        "cur_ask_amount": "✍️ Miqdorni {ccy} da kiriting (masalan: <code>1000</code>):",
        "cur_bad_amount": "❗️ Miqdorni raqamda kiriting (masalan: 1500).",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} so'm</b>\n\nKurs: 1 {ccy} = {rate} so'm ({date}, {src})",
        "cur_source_manual": "<i>Manba: O'zbekiston Markaziy banki (cbu.uz) rasmiy kursi, sana ko'rsatilgan.</i>",
        "cur_source_alt": "<i>Markaziy bank sayti javob bermadi, bozor kursi ko'rsatilmoqda (open.er-api.com). CBU kursidan biroz farq qilishi mumkin.</i>",
        "cur_error": "⚠️ Hozir Markaziy bank kurslarini olib bo'lmadi. Birozdan keyin qayta urinib ko'ring.",
        "lg_intro": "🚚 <b>Yuk tashishga buyurtma</b>\n\nBir nechta savolga javob bering, operatorimiz siz bilan bog'lanadi.",
        "lg_ask_origin": "📍 <b>Yuk qayerdan olinadi?</b>\n\nManzilni yozing yoki «📍 Lokatsiyani yuborish» tugmasini bosing.",
        "lg_ask_destination": "🏁 <b>Yuk qayerga yetkaziladi?</b>\n\nManzilni yozing yoki «📍 Lokatsiyani yuborish» tugmasini bosing.",
        "lg_btn_location": "📍 Lokatsiyani yuborish",
        "lg_bad_place": "❗️ Manzilni matn bilan yozing yoki lokatsiya yuboring.",
        "lg_ask_cargo": "📦 <b>Yuk turini tanlang:</b>",
        "lg_ask_cargo_other": "📦 Yuk turini yozing (masalan: <code>avto ehtiyot qismlar</code>):",
        "lg_ask_weight": "⚖️ <b>Yukning taxminiy og'irligi:</b>",
        "lg_ask_volume": "📐 <b>Yukning taxminiy hajmi:</b>",
        "lg_ask_ready": "⏰ <b>Yukingiz qachon tayyor bo'ladi?</b>",
        "lg_ask_ready_other": "📅 Sanani yozing (masalan: <code>15-noyabr</code>):",
        "lg_ask_phone": "📱 <b>Telefon raqamingiz</b>\n\n«📱 Raqamni yuborish» tugmasini bosing yoki raqamni yozing (masalan: <code>+998901234567</code>).",
        "lg_btn_phone": "📱 Raqamni yuborish",
        "lg_bad_phone": "❗️ Raqamni to'g'ri yozing (masalan: +998901234567) yoki tugmani bosing.",
        "lg_use_buttons": "👆 Iltimos, yuqoridagi tugmalardan birini tanlang.",
        "lg_confirm": "📋 <b>Buyurtmangiz:</b>\n\n{summary}\n\n<b>Hammasi to'g'rimi?</b>",
        "lg_btn_confirm": "✅ Ha, tasdiqlayman",
        "lg_btn_edit": "✏️ Tahrirlash",
        "lg_btn_drop": "❌ Bekor qilish",
        "lg_btn_back": "⬅️ Orqaga",
        "lg_edit_which": "Qaysi qatorni o'zgartirasiz?",
        "lg_thanks": "✅ <b>Buyurtmangiz qabul qilindi!</b>\n\nBuyurtma raqami: <b>#{no}</b>\nOperatorimiz tez orada siz bilan bog'lanadi.",
        "lg_admin": "🆕 <b>Yangi logistika buyurtmasi #{no}</b>\n\n👤 Mijoz: {who}\n\n{summary}",
        "lg_field": {
            "origin": "📍 Qayerdan",
            "destination": "🏁 Qayerga",
            "cargo": "📦 Yuk turi",
            "weight": "⚖️ Og'irligi",
            "volume": "📐 Hajmi",
            "ready": "⏰ Tayyor bo'ladi",
            "phone": "📱 Telefon",
        },
        "lg_cargo": {
            "furniture": "🛋 Mebel",
            "food": "🍎 Oziq-ovqat",
            "building": "🧱 Qurilish mollari",
            "appliances": "📺 Maishiy texnika",
            "textile": "👕 Kiyim / tekstil",
            "other": "✍️ Boshqa",
        },
        "lg_weight": {
            "w1": "100 kg gacha",
            "w2": "100–500 kg",
            "w3": "0.5–1.5 t",
            "w4": "1.5–5 t",
            "w5": "5–10 t",
            "w6": "10–20 t",
            "w7": "20 t dan ko'p",
        },
        "lg_volume": {
            "v1": "1 m³ gacha",
            "v2": "1–5 m³",
            "v3": "5–15 m³",
            "v4": "15–40 m³",
            "v5": "40–90 m³",
            "v6": "90 m³ dan ko'p",
            "unknown": "🤷 Bilmayman",
        },
        "lg_ready": {
            "now": "✅ Hozir tayyor",
            "today": "Bugun",
            "tomorrow": "Ertaga",
            "days": "2–3 kun ichida",
            "other": "📅 Boshqa sana",
        },
        # ---------- Sertifikat ----------
        "btn_cert": "📋 Sertifikat kerakmi?",
        "ct_intro": "📋 <b>Sertifikat kerakligini aniqlash</b>\n\nTovaringiz haqida bir nechta savolga javob bering, mutaxassisimiz tekshirib, javobni shu yerga yuboradi.",
        "ct_ask_product": "📦 <b>Tovar nomi va tavsifi</b>\n\nMasalan: <code>bolalar o'yinchog'i, plastik, 3 yoshdan</code>",
        "ct_ask_code": "🔢 <b>TIF TN kodi</b> (bilsangiz)\n\nBilmasangiz — «O'tkazib yuborish» ni bosing.",
        "ct_ask_country": "🌍 <b>Tovar qaysi davlatdan keladi?</b>",
        "ct_ask_purpose": "🎯 <b>Tovar nima uchun olib kelinmoqda?</b>",
        "ct_ask_file": "📎 <b>Tovar rasmi yoki hujjat</b> (invoys, yorliq)\n\nRasm yoki fayl yuboring. Yo'q bo'lsa — «O'tkazib yuborish» ni bosing.",
        "ct_bad_text": "❗️ Iltimos, matn bilan yozing.",
        "ct_bad_file": "❗️ Rasm yoki fayl yuboring, yoki «O'tkazib yuborish» ni bosing.",
        "ct_confirm": "📋 <b>Arizangiz:</b>\n\n{summary}\n\n<b>Hammasi to'g'rimi?</b>",
        "ct_thanks": "✅ <b>Arizangiz qabul qilindi!</b>\n\nAriza raqami: <b>#{no}</b>\nMutaxassisimiz tekshirib, javobni shu yerga yuboradi.",
        "ct_answer": "📋 <b>Mutaxassis javobi (ariza #{no}):</b>",
        "ct_file_yes": "📎 Biriktirilgan",
        "ct_none": "—",
        "ct_admin": "🆕 <b>Sertifikat bo'yicha ariza #{no}</b>\n\n👤 Mijoz: {who}\n\n{summary}",
        "ct_btn_reply": "✍️ Javob berish",
        "ct_ask_reply": "✍️ <b>#{no}</b> arizaga javobingizni yozing (matn, rasm yoki fayl). Mijozga bot orqali yuboriladi.",
        "ct_reply_sent": "✅ #{no} arizaga javob mijozga yuborildi.",
        "ct_reply_fail": "⚠️ #{no} arizaga javobni mijozga yuborib bo'lmadi (botni bloklagan bo'lishi mumkin).",
        "ct_field": {
            "product": "📦 Tovar",
            "code": "🔢 TIF TN kodi",
            "country": "🌍 Davlat",
            "purpose": "🎯 Maqsad",
            "file": "📎 Rasm / hujjat",
            "phone": "📱 Telefon",
        },
        "ct_purpose": {
            "sale": "🏪 Sotish uchun",
            "personal": "🏠 Shaxsiy foydalanish",
        },
    },
    "ru": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "Здравствуйте! Добро пожаловать в бот DCG Cargo! 🚚\n\nЛогистика, курсы валют и расчёт растаможки.",
        "bot_short_description": "Официальный бот DCG Cargo 🚚",
        "welcome": "👋 <b>Здравствуйте!</b>\n\n🚚 Добро пожаловать в бот <b>DCGCargo</b>!\n\nНажмите кнопку ниже 👇",
        "btn_calc": "🚗 Рассчитать растаможку",
        "btn_info": "ℹ️ Информация",
        "btn_lang": "🌐 Сменить язык",
        "btn_cancel": "❌ Отмена",
        "btn_skip": "⏭ Пропустить",
        "ask_fuel": "⛽️ Выберите тип топлива:",
        "fuel_ice": "⛽️ Бензин / Дизель",
        "fuel_hybrid": "🔋 Гибрид",
        "fuel_serial": "🔌 Последовательный гибрид (EREV)",
        "fuel_ev": "⚡️ Электро",
        "ask_year": "📅 Введите год выпуска (например: <code>2023</code>):",
        "bad_year": "❗️ Введите корректный год (например: 2022).",
        "ask_cc": "🔧 Введите объём двигателя в см³ (например: <code>1600</code>):",
        "bad_cc": "❗️ Введите объём числом (500 – 10000).",
        "ask_price": "💵 Введите стоимость авто в долларах США (например: <code>15000</code>):",
        "bad_num": "❗️ Введите число (например: 15000).",
        "ask_delivery": "🚚 Стоимость доставки ($)? Если не знаете — нажмите «Пропустить».",
        "cancelled": "Отменено.",
        "too_old": "⛔️ <b>Внимание:</b> ввоз бензиновых/дизельных авто старше {max} лет в Узбекистан запрещён (возраст авто: {age} лет). Расчёт только для информации.\n\n",
        "result": (
            "📊 <b>Результат расчёта</b>\n\n"
            "⛽️ Топливо: {fuel}\n"
            "📅 Год: {year} ({age} лет)\n"
            "{cc_line}"
            "💵 Цена: ${price}\n"
            "🚚 Доставка: ${delivery}\n"
            "🧾 Таможенная стоимость: ${value}\n"
            "💱 Курс: 1$ = {rate} сум\n\n"
            "━━━━━━━━━━━━━━━\n"
            "🏛 Таможенная пошлина: ${duty}\n"
            "🧮 НДС (12%): ${vat}\n"
            "♻️ Утильсбор: {util_brv} БРВ = {util} сум\n"
            "📑 Сбор за оформление: {clear} сум\n"
            "━━━━━━━━━━━━━━━\n"
            "💰 <b>Итого растаможка: {total} сум</b>\n"
            "≈ <b>${total_usd}</b>\n\n"
            "🚘 <b>Авто + растаможка ≈ ${grand}</b>\n\n"
            "⚠️ <i>Расчёт примерный. Точную сумму определяет таможня.</i>"
        ),
        "cc_line": "🔧 Двигатель: {cc} см³\n",
        "info": (
            "ℹ️ <b>Как работает расчёт</b>\n\n"
            "• Пошлина: до 1 года — 15% + $1/см³; 1–3 года — 30% + $2.5/см³; старше 3 лет — 40% + $3/см³\n"
            "• Электро и последовательные гибриды освобождены от пошлины\n"
            "• НДС: 12% (стоимость + пошлина)\n"
            "• Утильсбор: в БРВ, зависит от объёма и возраста\n"
            "• 1 БРВ = {brv} сум\n"
            "• Бензин/дизель: запрещены авто старше {max} лет, ниже Euro-5 и праворульные\n\n"
            "Курс берётся с сайта Центрального банка Узбекистана (cbu.uz)."
        ),
        # ---------- Логистика / валюта / поддержка ----------
        "btn_logistics": "🚚 Логистика",
        "btn_currency": "💱 Курс валют",
        "btn_support": "🆘 Поддержка",
        "support": (
            "🆘 <b>Поддержка</b>\n\n"
            "Если у вас есть вопросы, свяжитесь с администратором:\n\n"
            "{admins}\n"
            "📞 Телефон: {phone}"
        ),
        "support_btn_write": "✍️ Написать:",
        # ---------- Курс валют ----------
        "cur_title": "💱 <b>Курсы валют</b> ({date})",
        "cur_sum": "сум",
        "cur_source": "<i>Источник: Центральный банк Узбекистана (cbu.uz). ▲▼ — изменение к вчерашнему дню.</i>",
        "cur_btn_convert": "🧮 Перевести в сумы",
        "cur_btn_refresh": "🔄 Обновить",
        "cur_refreshed": "Курсы обновлены",
        "cur_pick": "🧮 Какую валюту перевести в сумы?",
        "cur_ask_amount": "✍️ Введите сумму в {ccy} (например: <code>1000</code>):",
        "cur_bad_amount": "❗️ Введите сумму числом (например: 1500).",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} сум</b>\n\nКурс: 1 {ccy} = {rate} сум ({date}, {src})",
        "cur_source_manual": "<i>Источник: официальный курс Центрального банка Узбекистана (cbu.uz) на указанную дату.</i>",
        "cur_source_alt": "<i>Сайт ЦБ не ответил, показан рыночный курс (open.er-api.com). Может немного отличаться от курса ЦБ.</i>",
        "cur_error": "⚠️ Сейчас не удалось получить курсы ЦБ. Попробуйте чуть позже.",
        "lg_intro": "🚚 <b>Заявка на перевозку груза</b>\n\nОтветьте на несколько вопросов, и наш оператор свяжется с вами.",
        "lg_ask_origin": "📍 <b>Откуда забрать груз?</b>\n\nНапишите адрес или нажмите «📍 Отправить локацию».",
        "lg_ask_destination": "🏁 <b>Куда доставить груз?</b>\n\nНапишите адрес или нажмите «📍 Отправить локацию».",
        "lg_btn_location": "📍 Отправить локацию",
        "lg_bad_place": "❗️ Напишите адрес текстом или отправьте локацию.",
        "lg_ask_cargo": "📦 <b>Выберите тип груза:</b>",
        "lg_ask_cargo_other": "📦 Напишите тип груза (например: <code>автозапчасти</code>):",
        "lg_ask_weight": "⚖️ <b>Примерный вес груза:</b>",
        "lg_ask_volume": "📐 <b>Примерный объём груза:</b>",
        "lg_ask_ready": "⏰ <b>Когда груз будет готов?</b>",
        "lg_ask_ready_other": "📅 Напишите дату (например: <code>15 ноября</code>):",
        "lg_ask_phone": "📱 <b>Ваш номер телефона</b>\n\nНажмите «📱 Отправить номер» или напишите номер (например: <code>+998901234567</code>).",
        "lg_btn_phone": "📱 Отправить номер",
        "lg_bad_phone": "❗️ Введите корректный номер (например: +998901234567) или нажмите кнопку.",
        "lg_use_buttons": "👆 Пожалуйста, выберите один из вариантов выше.",
        "lg_confirm": "📋 <b>Ваша заявка:</b>\n\n{summary}\n\n<b>Всё верно?</b>",
        "lg_btn_confirm": "✅ Да, подтверждаю",
        "lg_btn_edit": "✏️ Изменить",
        "lg_btn_drop": "❌ Отменить",
        "lg_btn_back": "⬅️ Назад",
        "lg_edit_which": "Что хотите изменить?",
        "lg_thanks": "✅ <b>Заявка принята!</b>\n\nНомер заявки: <b>#{no}</b>\nНаш оператор скоро свяжется с вами.",
        "lg_admin": "🆕 <b>Новая заявка на логистику #{no}</b>\n\n👤 Клиент: {who}\n\n{summary}",
        "lg_field": {
            "origin": "📍 Откуда",
            "destination": "🏁 Куда",
            "cargo": "📦 Тип груза",
            "weight": "⚖️ Вес",
            "volume": "📐 Объём",
            "ready": "⏰ Готовность",
            "phone": "📱 Телефон",
        },
        "lg_cargo": {
            "furniture": "🛋 Мебель",
            "food": "🍎 Продукты",
            "building": "🧱 Стройматериалы",
            "appliances": "📺 Бытовая техника",
            "textile": "👕 Одежда / текстиль",
            "other": "✍️ Другое",
        },
        "lg_weight": {
            "w1": "до 100 кг",
            "w2": "100–500 кг",
            "w3": "0.5–1.5 т",
            "w4": "1.5–5 т",
            "w5": "5–10 т",
            "w6": "10–20 т",
            "w7": "более 20 т",
        },
        "lg_volume": {
            "v1": "до 1 м³",
            "v2": "1–5 м³",
            "v3": "5–15 м³",
            "v4": "15–40 м³",
            "v5": "40–90 м³",
            "v6": "более 90 м³",
            "unknown": "🤷 Не знаю",
        },
        "lg_ready": {
            "now": "✅ Уже готов",
            "today": "Сегодня",
            "tomorrow": "Завтра",
            "days": "В течение 2–3 дней",
            "other": "📅 Другая дата",
        },
        # ---------- Сертификат ----------
        "btn_cert": "📋 Нужен сертификат?",
        "ct_intro": "📋 <b>Нужен ли сертификат</b>\n\nОтветьте на несколько вопросов о товаре — наш специалист проверит и пришлёт ответ сюда.",
        "ct_ask_product": "📦 <b>Название и описание товара</b>\n\nНапример: <code>детская игрушка, пластик, от 3 лет</code>",
        "ct_ask_code": "🔢 <b>Код ТН ВЭД</b> (если знаете)\n\nЕсли не знаете — нажмите «Пропустить».",
        "ct_ask_country": "🌍 <b>Из какой страны везёте товар?</b>",
        "ct_ask_purpose": "🎯 <b>Для чего ввозится товар?</b>",
        "ct_ask_file": "📎 <b>Фото товара или документ</b> (инвойс, этикетка)\n\nОтправьте фото или файл. Если нет — нажмите «Пропустить».",
        "ct_bad_text": "❗️ Пожалуйста, напишите текстом.",
        "ct_bad_file": "❗️ Отправьте фото или файл, либо нажмите «Пропустить».",
        "ct_confirm": "📋 <b>Ваша заявка:</b>\n\n{summary}\n\n<b>Всё верно?</b>",
        "ct_thanks": "✅ <b>Заявка принята!</b>\n\nНомер заявки: <b>#{no}</b>\nНаш специалист проверит и пришлёт ответ сюда.",
        "ct_answer": "📋 <b>Ответ специалиста (заявка #{no}):</b>",
        "ct_file_yes": "📎 Прикреплено",
        "ct_none": "—",
        "ct_field": {
            "product": "📦 Товар",
            "code": "🔢 Код ТН ВЭД",
            "country": "🌍 Страна",
            "purpose": "🎯 Цель",
            "file": "📎 Фото / документ",
            "phone": "📱 Телефон",
        },
        "ct_purpose": {
            "sale": "🏪 Для продажи",
            "personal": "🏠 Для личного пользования",
        },
    },
    "en": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "Hello! Welcome to the DCG Cargo bot! 🚚\n\nLogistics, currency rates and Uzbekistan car customs calculator.",
        "bot_short_description": "Official DCG Cargo bot 🚚",
        "welcome": "👋 <b>Hello!</b>\n\n🚚 Welcome to the <b>DCGCargo</b> bot!\n\nTap a button below 👇",
        "btn_calc": "🚗 Car customs calculator",
        "btn_info": "ℹ️ Info",
        "btn_lang": "🌐 Change language",
        "btn_cancel": "❌ Cancel",
        "btn_skip": "⏭ Skip",
        "ask_fuel": "⛽️ Choose the fuel type:",
        "fuel_ice": "⛽️ Petrol / Diesel",
        "fuel_hybrid": "🔋 Hybrid",
        "fuel_serial": "🔌 Series hybrid (EREV)",
        "fuel_ev": "⚡️ Electric",
        "ask_year": "📅 Enter the year of manufacture (e.g. <code>2023</code>):",
        "bad_year": "❗️ Please enter a valid year (e.g. 2022).",
        "ask_cc": "🔧 Enter the engine volume in cm³ (e.g. <code>1600</code>):",
        "bad_cc": "❗️ Enter the engine volume as a number (500 – 10000).",
        "ask_price": "💵 Enter the car price in US dollars (e.g. <code>15000</code>):",
        "bad_num": "❗️ Enter a number (e.g. 15000).",
        "ask_delivery": "🚚 Delivery cost ($)? If you don't know, tap «Skip».",
        "cancelled": "Cancelled.",
        "too_old": "⛔️ <b>Note:</b> importing petrol/diesel cars older than {max} years into Uzbekistan is prohibited (car age: {age} years). This calculation is for information only.\n\n",
        "result": (
            "📊 <b>Calculation result</b>\n\n"
            "⛽️ Fuel: {fuel}\n"
            "📅 Year: {year} ({age} years)\n"
            "{cc_line}"
            "💵 Price: ${price}\n"
            "🚚 Delivery: ${delivery}\n"
            "🧾 Customs value: ${value}\n"
            "💱 Rate: 1$ = {rate} UZS\n\n"
            "━━━━━━━━━━━━━━━\n"
            "🏛 Customs duty: ${duty}\n"
            "🧮 VAT (12%): ${vat}\n"
            "♻️ Recycling fee: {util_brv} BCV = {util} UZS\n"
            "📑 Clearance fee: {clear} UZS\n"
            "━━━━━━━━━━━━━━━\n"
            "💰 <b>Total customs payments: {total} UZS</b>\n"
            "≈ <b>${total_usd}</b>\n\n"
            "🚘 <b>Car + customs ≈ ${grand}</b>\n\n"
            "⚠️ <i>This is an estimate. The exact amount is set by customs.</i>"
        ),
        "cc_line": "🔧 Engine: {cc} cm³\n",
        "info": (
            "ℹ️ <b>How the calculation works</b>\n\n"
            "• Customs duty: up to 1 year — 15% + $1/cm³; 1–3 years — 30% + $2.5/cm³; over 3 years — 40% + $3/cm³\n"
            "• Electric cars and series hybrids are exempt from duty\n"
            "• VAT: 12% (value + duty)\n"
            "• Recycling fee: in BCV, depends on engine volume and age\n"
            "• 1 BCV (base calculation value) = {brv} UZS\n"
            "• Petrol/diesel: cars older than {max} years, below Euro-5 and right-hand drive are prohibited\n\n"
            "Rates are taken from the Central Bank of Uzbekistan (cbu.uz)."
        ),
        # ---------- Logistics / currency / support ----------
        "btn_logistics": "🚚 Logistics",
        "btn_currency": "💱 Currency rates",
        "btn_support": "🆘 Support",
        "support": (
            "🆘 <b>Support</b>\n\n"
            "If you have any questions, contact our administrators:\n\n"
            "{admins}\n"
            "📞 Phone: {phone}"
        ),
        "support_btn_write": "✍️ Message:",
        # ---------- Currency rates ----------
        "cur_title": "💱 <b>Currency rates</b> ({date})",
        "cur_sum": "UZS",
        "cur_source": "<i>Source: Central Bank of Uzbekistan (cbu.uz). ▲▼ — change since yesterday.</i>",
        "cur_btn_convert": "🧮 Convert to UZS",
        "cur_btn_refresh": "🔄 Refresh",
        "cur_refreshed": "Rates updated",
        "cur_pick": "🧮 Which currency do you want to convert to UZS?",
        "cur_ask_amount": "✍️ Enter the amount in {ccy} (e.g. <code>1000</code>):",
        "cur_bad_amount": "❗️ Enter the amount as a number (e.g. 1500).",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} UZS</b>\n\nRate: 1 {ccy} = {rate} UZS ({date}, {src})",
        "cur_source_manual": "<i>Source: official rate of the Central Bank of Uzbekistan (cbu.uz) for the date shown.</i>",
        "cur_source_alt": "<i>The Central Bank website did not respond, showing the market rate (open.er-api.com). It may differ slightly from the CBU rate.</i>",
        "cur_error": "⚠️ Could not get the Central Bank rates right now. Please try again a bit later.",
        "lg_intro": "🚚 <b>Cargo transportation request</b>\n\nAnswer a few questions and our operator will contact you.",
        "lg_ask_origin": "📍 <b>Where should the cargo be picked up?</b>\n\nType the address or tap «📍 Send location».",
        "lg_ask_destination": "🏁 <b>Where should the cargo be delivered?</b>\n\nType the address or tap «📍 Send location».",
        "lg_btn_location": "📍 Send location",
        "lg_bad_place": "❗️ Type the address as text or send a location.",
        "lg_ask_cargo": "📦 <b>Choose the cargo type:</b>",
        "lg_ask_cargo_other": "📦 Type the cargo type (e.g. <code>car spare parts</code>):",
        "lg_ask_weight": "⚖️ <b>Approximate cargo weight:</b>",
        "lg_ask_volume": "📐 <b>Approximate cargo volume:</b>",
        "lg_ask_ready": "⏰ <b>When will the cargo be ready?</b>",
        "lg_ask_ready_other": "📅 Type the date (e.g. <code>15 November</code>):",
        "lg_ask_phone": "📱 <b>Your phone number</b>\n\nTap «📱 Send number» or type your number (e.g. <code>+998901234567</code>).",
        "lg_btn_phone": "📱 Send number",
        "lg_bad_phone": "❗️ Enter a valid number (e.g. +998901234567) or tap the button.",
        "lg_use_buttons": "👆 Please choose one of the options above.",
        "lg_confirm": "📋 <b>Your request:</b>\n\n{summary}\n\n<b>Is everything correct?</b>",
        "lg_btn_confirm": "✅ Yes, confirm",
        "lg_btn_edit": "✏️ Edit",
        "lg_btn_drop": "❌ Cancel",
        "lg_btn_back": "⬅️ Back",
        "lg_edit_which": "What would you like to change?",
        "lg_thanks": "✅ <b>Your request has been received!</b>\n\nRequest number: <b>#{no}</b>\nOur operator will contact you soon.",
        "lg_admin": "🆕 <b>New logistics request #{no}</b>\n\n👤 Client: {who}\n\n{summary}",
        "lg_field": {
            "origin": "📍 From",
            "destination": "🏁 To",
            "cargo": "📦 Cargo type",
            "weight": "⚖️ Weight",
            "volume": "📐 Volume",
            "ready": "⏰ Ready",
            "phone": "📱 Phone",
        },
        "lg_cargo": {
            "furniture": "🛋 Furniture",
            "food": "🍎 Food",
            "building": "🧱 Building materials",
            "appliances": "📺 Home appliances",
            "textile": "👕 Clothing / textiles",
            "other": "✍️ Other",
        },
        "lg_weight": {
            "w1": "up to 100 kg",
            "w2": "100–500 kg",
            "w3": "0.5–1.5 t",
            "w4": "1.5–5 t",
            "w5": "5–10 t",
            "w6": "10–20 t",
            "w7": "over 20 t",
        },
        "lg_volume": {
            "v1": "up to 1 m³",
            "v2": "1–5 m³",
            "v3": "5–15 m³",
            "v4": "15–40 m³",
            "v5": "40–90 m³",
            "v6": "over 90 m³",
            "unknown": "🤷 Don't know",
        },
        "lg_ready": {
            "now": "✅ Ready now",
            "today": "Today",
            "tomorrow": "Tomorrow",
            "days": "Within 2–3 days",
            "other": "📅 Other date",
        },
        # ---------- Certificate ----------
        "btn_cert": "📋 Need a certificate?",
        "ct_intro": "📋 <b>Do you need a certificate?</b>\n\nAnswer a few questions about your goods — our specialist will check and send the answer here.",
        "ct_ask_product": "📦 <b>Product name and description</b>\n\nFor example: <code>children's toy, plastic, 3+ years</code>",
        "ct_ask_code": "🔢 <b>HS code</b> (if you know it)\n\nIf not — press «Skip».",
        "ct_ask_country": "🌍 <b>Which country are the goods coming from?</b>",
        "ct_ask_purpose": "🎯 <b>What are the goods imported for?</b>",
        "ct_ask_file": "📎 <b>Product photo or document</b> (invoice, label)\n\nSend a photo or file. If you don't have one — press «Skip».",
        "ct_bad_text": "❗️ Please type it as text.",
        "ct_bad_file": "❗️ Send a photo or file, or press «Skip».",
        "ct_confirm": "📋 <b>Your request:</b>\n\n{summary}\n\n<b>Is everything correct?</b>",
        "ct_thanks": "✅ <b>Request received!</b>\n\nRequest number: <b>#{no}</b>\nOur specialist will check and send the answer here.",
        "ct_answer": "📋 <b>Specialist's answer (request #{no}):</b>",
        "ct_file_yes": "📎 Attached",
        "ct_none": "—",
        "ct_field": {
            "product": "📦 Product",
            "code": "🔢 HS code",
            "country": "🌍 Country",
            "purpose": "🎯 Purpose",
            "file": "📎 Photo / document",
            "phone": "📱 Phone",
        },
        "ct_purpose": {
            "sale": "🏪 For sale",
            "personal": "🏠 Personal use",
        },
    },
    "zh": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "您好！欢迎使用 DCG Cargo 机器人！🚚\n\n物流服务、汇率查询及乌兹别克斯坦汽车清关费用计算。",
        "bot_short_description": "DCG Cargo 官方机器人 🚚",
        "welcome": "👋 <b>您好！</b>\n\n🚚 欢迎使用 <b>DCGCargo</b> 机器人！\n\n请点击下方按钮 👇",
        "btn_calc": "🚗 汽车清关费用计算",
        "btn_info": "ℹ️ 说明",
        "btn_lang": "🌐 切换语言",
        "btn_cancel": "❌ 取消",
        "btn_skip": "⏭ 跳过",
        "ask_fuel": "⛽️ 请选择燃料类型：",
        "fuel_ice": "⛽️ 汽油 / 柴油",
        "fuel_hybrid": "🔋 混合动力",
        "fuel_serial": "🔌 增程式混合动力 (EREV)",
        "fuel_ev": "⚡️ 纯电动",
        "ask_year": "📅 请输入生产年份（例如：<code>2023</code>）：",
        "bad_year": "❗️ 请输入正确的年份（例如：2022）。",
        "ask_cc": "🔧 请输入发动机排量，单位 cm³（例如：<code>1600</code>）：",
        "bad_cc": "❗️ 请用数字输入排量（500 – 10000）。",
        "ask_price": "💵 请输入车辆价格，单位美元（例如：<code>15000</code>）：",
        "bad_num": "❗️ 请输入数字（例如：15000）。",
        "ask_delivery": "🚚 运费是多少（$）？如果不清楚，请点击「跳过」。",
        "cancelled": "已取消。",
        "too_old": "⛔️ <b>注意：</b>车龄超过 {max} 年的汽油/柴油车禁止进口到乌兹别克斯坦（该车车龄：{age} 年）。以下计算仅供参考。\n\n",
        "result": (
            "📊 <b>计算结果</b>\n\n"
            "⛽️ 燃料：{fuel}\n"
            "📅 年份：{year}（{age} 年）\n"
            "{cc_line}"
            "💵 价格：${price}\n"
            "🚚 运费：${delivery}\n"
            "🧾 完税价格：${value}\n"
            "💱 汇率：1$ = {rate} 苏姆\n\n"
            "━━━━━━━━━━━━━━━\n"
            "🏛 关税：${duty}\n"
            "🧮 增值税（12%）：${vat}\n"
            "♻️ 回收费：{util_brv} BCV = {util} 苏姆\n"
            "📑 报关手续费：{clear} 苏姆\n"
            "━━━━━━━━━━━━━━━\n"
            "💰 <b>清关费用合计：{total} 苏姆</b>\n"
            "≈ <b>${total_usd}</b>\n\n"
            "🚘 <b>车价 + 清关 ≈ ${grand}</b>\n\n"
            "⚠️ <i>以上为估算，准确金额以海关核定为准。</i>"
        ),
        "cc_line": "🔧 排量：{cc} cm³\n",
        "info": (
            "ℹ️ <b>计算说明</b>\n\n"
            "• 关税：1 年以内 — 15% + $1/cm³；1–3 年 — 30% + $2.5/cm³；3 年以上 — 40% + $3/cm³\n"
            "• 纯电动车和增程式混合动力车免征关税\n"
            "• 增值税：12%（完税价格 + 关税）\n"
            "• 回收费：以 BCV 计，取决于排量和车龄\n"
            "• 1 BCV（基本计算单位）= {brv} 苏姆\n"
            "• 汽油/柴油车：禁止进口车龄超过 {max} 年、低于欧5排放标准及右舵车辆\n\n"
            "汇率来源：乌兹别克斯坦中央银行（cbu.uz）。"
        ),
        # ---------- 物流 / 汇率 / 客服 ----------
        "btn_logistics": "🚚 物流",
        "btn_currency": "💱 汇率",
        "btn_support": "🆘 客服",
        "support": (
            "🆘 <b>客服</b>\n\n"
            "如有任何问题，请联系我们的管理员：\n\n"
            "{admins}\n"
            "📞 电话：{phone}"
        ),
        "support_btn_write": "✍️ 联系：",
        # ---------- 汇率 ----------
        "cur_title": "💱 <b>汇率</b>（{date}）",
        "cur_sum": "苏姆",
        "cur_source": "<i>来源：乌兹别克斯坦中央银行（cbu.uz）。▲▼ — 与昨日相比的变化。</i>",
        "cur_btn_convert": "🧮 换算成苏姆",
        "cur_btn_refresh": "🔄 刷新",
        "cur_refreshed": "汇率已更新",
        "cur_pick": "🧮 请选择要换算成苏姆的货币：",
        "cur_ask_amount": "✍️ 请输入 {ccy} 金额（例如：<code>1000</code>）：",
        "cur_bad_amount": "❗️ 请用数字输入金额（例如：1500）。",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} 苏姆</b>\n\n汇率：1 {ccy} = {rate} 苏姆（{date}，{src}）",
        "cur_source_manual": "<i>来源：乌兹别克斯坦中央银行（cbu.uz）在所示日期的官方汇率。</i>",
        "cur_source_alt": "<i>中央银行网站未响应，当前显示市场汇率（open.er-api.com），可能与央行汇率略有差异。</i>",
        "cur_error": "⚠️ 暂时无法获取中央银行汇率，请稍后再试。",
        "lg_intro": "🚚 <b>货运下单</b>\n\n请回答几个问题，我们的客服会尽快与您联系。",
        "lg_ask_origin": "📍 <b>在哪里提货？</b>\n\n请输入地址或点击「📍 发送位置」。",
        "lg_ask_destination": "🏁 <b>货物送到哪里？</b>\n\n请输入地址或点击「📍 发送位置」。",
        "lg_btn_location": "📍 发送位置",
        "lg_bad_place": "❗️ 请输入文字地址或发送位置。",
        "lg_ask_cargo": "📦 <b>请选择货物类型：</b>",
        "lg_ask_cargo_other": "📦 请输入货物类型（例如：<code>汽车配件</code>）：",
        "lg_ask_weight": "⚖️ <b>货物大概重量：</b>",
        "lg_ask_volume": "📐 <b>货物大概体积：</b>",
        "lg_ask_ready": "⏰ <b>货物什么时候准备好？</b>",
        "lg_ask_ready_other": "📅 请输入日期（例如：<code>11月15日</code>）：",
        "lg_ask_phone": "📱 <b>您的电话号码</b>\n\n请点击「📱 发送号码」或直接输入号码（例如：<code>+998901234567</code>）。",
        "lg_btn_phone": "📱 发送号码",
        "lg_bad_phone": "❗️ 请输入正确的号码（例如：+998901234567）或点击按钮。",
        "lg_use_buttons": "👆 请选择上方的一个选项。",
        "lg_confirm": "📋 <b>您的订单：</b>\n\n{summary}\n\n<b>信息是否正确？</b>",
        "lg_btn_confirm": "✅ 确认",
        "lg_btn_edit": "✏️ 修改",
        "lg_btn_drop": "❌ 取消",
        "lg_btn_back": "⬅️ 返回",
        "lg_edit_which": "您要修改哪一项？",
        "lg_thanks": "✅ <b>订单已收到！</b>\n\n订单号：<b>#{no}</b>\n我们的客服会尽快与您联系。",
        "lg_admin": "🆕 <b>新物流订单 #{no}</b>\n\n👤 客户：{who}\n\n{summary}",
        "lg_field": {
            "origin": "📍 起运地",
            "destination": "🏁 目的地",
            "cargo": "📦 货物类型",
            "weight": "⚖️ 重量",
            "volume": "📐 体积",
            "ready": "⏰ 备货时间",
            "phone": "📱 电话",
        },
        "lg_cargo": {
            "furniture": "🛋 家具",
            "food": "🍎 食品",
            "building": "🧱 建筑材料",
            "appliances": "📺 家用电器",
            "textile": "👕 服装 / 纺织品",
            "other": "✍️ 其他",
        },
        "lg_weight": {
            "w1": "100 公斤以内",
            "w2": "100–500 公斤",
            "w3": "0.5–1.5 吨",
            "w4": "1.5–5 吨",
            "w5": "5–10 吨",
            "w6": "10–20 吨",
            "w7": "20 吨以上",
        },
        "lg_volume": {
            "v1": "1 m³ 以内",
            "v2": "1–5 m³",
            "v3": "5–15 m³",
            "v4": "15–40 m³",
            "v5": "40–90 m³",
            "v6": "90 m³ 以上",
            "unknown": "🤷 不清楚",
        },
        "lg_ready": {
            "now": "✅ 已备好",
            "today": "今天",
            "tomorrow": "明天",
            "days": "2–3 天内",
            "other": "📅 其他日期",
        },
        # ---------- 证书 ----------
        "btn_cert": "📋 需要证书吗？",
        "ct_intro": "📋 <b>是否需要证书</b>\n\n请回答几个关于货物的问题，我们的专家核实后会在这里回复您。",
        "ct_ask_product": "📦 <b>商品名称和描述</b>\n\n例如：<code>儿童玩具，塑料，3岁以上</code>",
        "ct_ask_code": "🔢 <b>海关编码 (HS)</b>（如果知道）\n\n不知道请点击「跳过」。",
        "ct_ask_country": "🌍 <b>货物从哪个国家运来？</b>",
        "ct_ask_purpose": "🎯 <b>货物进口用途是什么？</b>",
        "ct_ask_file": "📎 <b>商品照片或文件</b>（发票、标签）\n\n请发送照片或文件。没有请点击「跳过」。",
        "ct_bad_text": "❗️ 请用文字输入。",
        "ct_bad_file": "❗️ 请发送照片或文件，或点击「跳过」。",
        "ct_confirm": "📋 <b>您的申请：</b>\n\n{summary}\n\n<b>信息正确吗？</b>",
        "ct_thanks": "✅ <b>申请已收到！</b>\n\n申请编号：<b>#{no}</b>\n我们的专家核实后会在这里回复您。",
        "ct_answer": "📋 <b>专家回复（申请 #{no}）：</b>",
        "ct_file_yes": "📎 已附加",
        "ct_none": "—",
        "ct_field": {
            "product": "📦 商品",
            "code": "🔢 海关编码",
            "country": "🌍 国家",
            "purpose": "🎯 用途",
            "file": "📎 照片 / 文件",
            "phone": "📱 电话",
        },
        "ct_purpose": {
            "sale": "🏪 用于销售",
            "personal": "🏠 个人使用",
        },
    },
}
