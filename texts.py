"""Bot matnlari: oʻzbek (uz), rus (ru), ingliz (en) va xitoy (zh)."""

CHOOSE_LANG = "🌐 Tilni tanlang / Выберите язык / Choose language / 选择语言:"

T = {
    "uz": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "Assalomu alaykum! DCG Cargo botiga xush kelibsiz! 🚚\n\nLogistika, valyuta kursi va avtomobil bojxona toʻlovlari hisobi.",
        "bot_short_description": "DCG Cargo rasmiy boti 🚚",
        "welcome": "👋 <b>Assalomu alaykum!</b>\n\n🚚 <b>DCG Cargo</b> botiga xush kelibsiz!\n\nKerakli boʻlimni tanlang 👇",
        "btn_calc": "💰 Bojxona kalkulyatori",
        "btn_info": "ℹ️ Maʼlumot",
        "btn_lang": "🌐 Til",
        "btn_cancel": "❌ Bekor qilish",
        "btn_skip": "⏭ Oʻtkazib yuborish",
        "ask_fuel": "⛽️ Yoqilgʻi turini tanlang:",
        "fuel_ice": "⛽️ Benzin / Dizel",
        "fuel_hybrid": "🔋 Gibrid",
        "fuel_serial": "🔌 Ketma-ket gibrid (EREV)",
        "fuel_ev": "⚡️ Elektr",
        "ask_year": "📅 Ishlab chiqarilgan yilni kiriting (masalan: <code>2023</code>):",
        "bad_year": "❗️ Yilni toʻgʻri kiriting (masalan: 2022).",
        "ask_cc": "🔧 Dvigatel hajmini sm³ da kiriting (masalan: <code>1600</code>):",
        "bad_cc": "❗️ Dvigatel hajmini raqamda kiriting (500 – 10000).",
        "ask_price": "💵 Avtomobil narxini AQSh dollarida kiriting (masalan: <code>15000</code>):",
        "bad_num": "❗️ Raqam kiriting (masalan: 15000).",
        "ask_delivery": "🚚 Yetkazib berish narxi ($)? Bilmasangiz, «Oʻtkazib yuborish»ni bosing.",
        "cancelled": "Bekor qilindi.",
        "too_old": "⛔️ <b>Diqqat:</b> {max} yildan eski benzin/dizel avtomobillarni Oʻzbekistonga olib kirish taqiqlangan (avtomobil yoshi: {age} yil). Hisob faqat maʼlumot uchun.\n\n",
        "result": (
            "📊 <b>Hisob natijasi</b>\n\n"
            "⛽️ Yoqilgʻi: {fuel}\n"
            "📅 Yili: {year} ({age} yil)\n"
            "{cc_line}"
            "💵 Narxi: ${price}\n"
            "🚚 Yetkazish: ${delivery}\n"
            "🧾 Bojxona qiymati: ${value}\n"
            "💱 Kurs: 1$ = {rate} soʻm\n\n"
            "━━━━━━━━━━━━━━━\n"
            "🏛 Bojxona boji: ${duty}\n"
            "🧮 QQS (12%): ${vat}\n"
            "♻️ Utilizatsiya yigʻimi: {util_brv} BHM = {util} soʻm\n"
            "📑 Rasmiylashtirish yigʻimi: {clear} soʻm\n"
            "━━━━━━━━━━━━━━━\n"
            "💰 <b>Jami bojxona toʻlovlari: {total} soʻm</b>\n"
            "≈ <b>${total_usd}</b>\n\n"
            "🚘 <b>Avtomobil + bojxona ≈ ${grand}</b>\n\n"
            "⚠️ <i>Hisob taxminiy. Aniq summani bojxona belgilaydi.</i>"
        ),
        "cc_line": "🔧 Dvigatel: {cc} sm³\n",
        "info": (
            "ℹ️ <b>Hisob qanday qilinadi</b>\n\n"
            "• Bojxona boji: 1 yilgacha — 15% + $1/sm³; 1–3 yil — 30% + $2.5/sm³; 3 yildan oshiq — 40% + $3/sm³\n"
            "• Elektr va ketma-ket gibrid avtomobillar bojdan ozod\n"
            "• QQS: 12% (qiymat + boj)\n"
            "• Utilizatsiya yigʻimi: BHM da, dvigatel hajmi va yoshiga qarab\n"
            "• 1 BHM = {brv} soʻm\n"
            "• Benzin/dizel: {max} yildan eski, Euro-5 dan past va oʻng rulli avtomobillar taqiqlangan\n\n"
            "Kurs Oʻzbekiston Markaziy bankidan (cbu.uz) olinadi."
        ),
        # ---------- Logistika / valyuta / yordam ----------
        "btn_logistics": "🚛 Xalqaro logistika",
        "btn_currency": "💱 Valyuta kursi",
        "btn_declarant": "👨‍💼 Deklarant xizmati",
        "staff_title": "👨‍💼 <b>Deklarant xizmati</b>\n\nKerakli xodimni tanlang. 📞 tugmasini bossangiz, uning raqami keladi.",
        "staff_role": {
            "declarant": "🧾 Deklarantlar",
            "logistics": "🚛 Logistika",
            "manager": "💼 Menejerlar",
        },
        "btn_support": "📞 Menejer bilan bogʻlanish",
        "support": (
            "📞 <b>Menejer bilan bogʻlanish</b>\n\n"
            "Savollaringiz boʻlsa, menejerimizga yozing:\n\n"
            "{admins}\n"
            "📞 Telefon: {phone}"
        ),
        "support_btn_write": "✍️ Yozish:",
        # ---------- Valyuta kursi ----------
        "cur_title": "💱 <b>Valyuta kurslari</b> ({date})",
        "cur_sum": "soʻm",
        "cur_source": "<i>Manba: Oʻzbekiston Markaziy banki (cbu.uz). ▲▼ — kechagi kunga nisbatan.</i>",
        "cur_btn_convert": "🧮 Soʻmga hisoblash",
        "cur_btn_refresh": "🔄 Yangilash",
        "cur_refreshed": "Kurslar yangilandi",
        "cur_pick": "🧮 Qaysi valyutani soʻmga hisoblaymiz?",
        "cur_ask_amount": "✍️ Miqdorni {ccy} da kiriting (masalan: <code>1000</code>):",
        "cur_bad_amount": "❗️ Miqdorni raqamda kiriting (masalan: 1500).",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} soʻm</b>\n\nKurs: 1 {ccy} = {rate} soʻm ({date}, {src})",
        "cur_source_manual": "<i>Manba: Oʻzbekiston Markaziy bankining (cbu.uz) rasmiy kursi.</i>",
        "cur_source_alt": "<i>Markaziy bank sayti javob bermadi, bozor kursi koʻrsatildi (open.er-api.com). U rasmiy kursdan biroz farq qilishi mumkin.</i>",
        "cur_error": "⚠️ Hozir kurslarni olib boʻlmadi. Birozdan keyin qayta urinib koʻring.",
        "lg_intro": "🚚 <b>Yuk tashishga buyurtma</b>\n\nBir nechta savolga javob bering, operatorimiz siz bilan bogʻlanadi.",
        "lg_ask_origin": "📍 <b>Yuk qayerdan olinadi?</b>\n\nManzilni yozing yoki «📍 Joylashuvni yuborish»ni bosing.",
        "lg_ask_destination": "🏁 <b>Yuk qayerga yetkaziladi?</b>\n\nManzilni yozing yoki «📍 Joylashuvni yuborish»ni bosing.",
        "lg_btn_location": "📍 Joylashuvni yuborish",
        "lg_bad_place": "❗️ Manzilni matn bilan yozing yoki joylashuv yuboring.",
        "lg_ask_cargo": "📦 <b>Yuk turini tanlang:</b>",
        "lg_ask_cargo_other": "📦 Yuk turini yozing (masalan: <code>avto ehtiyot qismlari</code>):",
        "lg_ask_weight": "⚖️ <b>Yukning taxminiy ogʻirligi:</b>",
        "lg_ask_volume": "📐 <b>Yukning taxminiy hajmi:</b>",
        "lg_ask_ready": "⏰ <b>Yuk qachon tayyor boʻladi?</b>",
        "lg_ask_ready_other": "📅 Sanani yozing (masalan: <code>15-noyabr</code>):",
        "lg_ask_phone": "📱 <b>Telefon raqamingiz</b>\n\n«📱 Raqamni yuborish»ni bosing yoki raqamni yozing (masalan: <code>+998901234567</code>).",
        "lg_btn_phone": "📱 Raqamni yuborish",
        "lg_bad_phone": "❗️ Raqamni toʻgʻri yozing (masalan: +998901234567) yoki tugmani bosing.",
        "lg_use_buttons": "👆 Yuqoridagi tugmalardan birini tanlang.",
        "lg_confirm": "📋 <b>Buyurtmangiz:</b>\n\n{summary}\n\n<b>Hammasi toʻgʻrimi?</b>",
        "lg_btn_confirm": "✅ Tasdiqlash",
        "lg_btn_edit": "✏️ Tahrirlash",
        "lg_btn_drop": "❌ Bekor qilish",
        "lg_btn_back": "⬅️ Orqaga",
        "lg_edit_which": "Qaysi maʼlumotni oʻzgartirasiz?",
        "lg_thanks": "✅ <b>Buyurtmangiz qabul qilindi!</b>\n\nBuyurtma raqami: <b>#{no}</b>\nOperatorimiz tez orada siz bilan bogʻlanadi.",
        "lg_admin": "🆕 <b>Yangi logistika buyurtmasi #{no}</b>\n\n👤 Mijoz: {who}\n\n{summary}",
        "lg_field": {
            "origin": "📍 Qayerdan",
            "destination": "🏁 Qayerga",
            "cargo": "📦 Yuk turi",
            "weight": "⚖️ Ogʻirligi",
            "volume": "📐 Hajmi",
            "ready": "⏰ Tayyor boʻlishi",
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
            "w7": "20 t dan koʻp",
        },
        "lg_volume": {
            "v1": "1 m³ gacha",
            "v2": "1–5 m³",
            "v3": "5–15 m³",
            "v4": "15–40 m³",
            "v5": "40–90 m³",
            "v6": "90 m³ dan koʻp",
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
        "btn_cert": "📑 Sertifikatlashtirish",
        "ct_intro": "📋 <b>Sertifikat kerakmi?</b>\n\nTovar haqida bir nechta savolga javob bering. Mutaxassisimiz tekshirib, javobni shu yerga yuboradi.",
        "ct_ask_product": "📦 <b>Tovar nomi va tavsifi</b>\n\nMasalan: <code>bolalar oʻyinchogʻi, plastik, 3 yoshdan</code>",
        "ct_ask_code": "🔢 <b>TIF TN kodi</b> (bilsangiz)\n\nBilmasangiz, «Oʻtkazib yuborish»ni bosing.",
        "ct_ask_country": "🌍 <b>Tovar qaysi davlatdan keladi?</b>",
        "ct_ask_purpose": "🎯 <b>Tovar nima maqsadda olib kelinmoqda?</b>",
        "ct_ask_file": "📎 <b>Tovar rasmi yoki hujjati</b> (invoys, yorliq)\n\nRasm yoki fayl yuboring. Boʻlmasa, «Oʻtkazib yuborish»ni bosing.",
        "ct_bad_text": "❗️ Matn bilan yozing.",
        "ct_bad_file": "❗️ Rasm yoki fayl yuboring yoki «Oʻtkazib yuborish»ni bosing.",
        "ct_confirm": "📋 <b>Arizangiz:</b>\n\n{summary}\n\n<b>Hammasi toʻgʻrimi?</b>",
        "ct_thanks": "✅ <b>Arizangiz qabul qilindi!</b>\n\nAriza raqami: <b>#{no}</b>\nMutaxassisimiz javobni shu yerga yuboradi.",
        "ct_answer": "📋 <b>Mutaxassis javobi (ariza #{no}):</b>",
        "ct_file_yes": "📎 Biriktirilgan",
        "ct_none": "—",
        "ct_admin": "🆕 <b>Sertifikat boʻyicha ariza #{no}</b>\n\n👤 Mijoz: {who}\n\n{summary}",
        "ct_btn_reply": "✍️ Javob berish",
        "ct_ask_reply": "✍️ <b>#{no}</b> arizaga javob yozing (matn, rasm yoki fayl). Javob mijozga bot orqali yuboriladi.",
        "ct_reply_sent": "✅ #{no} arizaga javob mijozga yuborildi.",
        "ct_reply_fail": "⚠️ #{no} arizaga javobni yuborib boʻlmadi (mijoz botni bloklagan boʻlishi mumkin).",
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
            "personal": "🏠 Shaxsiy foydalanish uchun",
        },
        "btn_trade": "📦 Import / Eksport",
        "tr_intro": "🌍 <b>Import / eksport buyurtmasi</b>\n\nBir nechta savolga javob bering, menejerimiz siz bilan bogʻlanadi.\n\n❗️ Buyurtma faqat <b>telefon raqami</b> bilan qabul qilinadi.",
        "tr_ask_direction": "🔀 <b>Qaysi xizmat kerak?</b>",
        "tr_ask_product": "📦 <b>Tovar nomi</b>\n\nMasalan: <code>maishiy texnika, 2 ta konteyner</code>",
        "tr_ask_country_import": "🌍 <b>Tovar qaysi davlatdan olib kelinadi?</b>",
        "tr_ask_country_export": "🌍 <b>Tovar qaysi davlatga olib chiqiladi?</b>",
        "tr_ask_volume": "⚖️ <b>Taxminiy hajmi yoki ogʻirligi</b>\n\nMasalan: <code>20 tonna</code>, <code>1 fura</code>. Bilmasangiz, «Oʻtkazib yuborish»ni bosing.",
        "tr_ask_name": "👤 <b>Ismingiz yoki kompaniya nomi</b>",
        "tr_ask_phone": "📱 <b>Telefon raqamingiz (majburiy)</b>\n\n«📱 Raqamni yuborish»ni bosing yoki raqamni yozing (masalan: <code>+998901234567</code>).",
        "tr_bad_phone": "❗️ Telefon raqami majburiy. Raqamni toʻgʻri yozing (masalan: +998901234567) yoki «📱 Raqamni yuborish»ni bosing.",
        "tr_confirm": "🌍 <b>Buyurtmangiz:</b>\n\n{summary}\n\n<b>Hammasi toʻgʻrimi?</b>",
        "tr_thanks": "✅ <b>Buyurtmangiz qabul qilindi!</b>\n\nBuyurtma raqami: <b>#{no}</b>\nMenejerimiz tez orada siz bilan bogʻlanadi.",
        "tr_admin": "🆕 <b>Import / eksport buyurtmasi #{no}</b>\n\n👤 Mijoz: {who}\n\n{summary}",
        "tr_field": {
            "direction": "🔀 Xizmat",
            "product": "📦 Tovar",
            "country": "🌍 Davlat",
            "volume": "⚖️ Hajmi",
            "name": "👤 Ism / kompaniya",
            "phone": "📱 Telefon",
        },
        "tr_direction": {
            "import": "📥 Import",
            "export": "📤 Eksport",
        },
    },
    "ru": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "Здравствуйте! Добро пожаловать в бот DCG Cargo! 🚚\n\nЛогистика, курсы валют и расчёт растаможки авто.",
        "bot_short_description": "Официальный бот DCG Cargo 🚚",
        "welcome": "👋 <b>Здравствуйте!</b>\n\n🚚 Добро пожаловать в бот <b>DCG Cargo</b>!\n\nВыберите нужный раздел 👇",
        "btn_calc": "💰 Таможенный калькулятор",
        "btn_info": "ℹ️ Справка",
        "btn_lang": "🌐 Язык",
        "btn_cancel": "❌ Отмена",
        "btn_skip": "⏭ Пропустить",
        "ask_fuel": "⛽️ Выберите тип топлива:",
        "fuel_ice": "⛽️ Бензин / Дизель",
        "fuel_hybrid": "🔋 Гибрид",
        "fuel_serial": "🔌 Последовательный гибрид (EREV)",
        "fuel_ev": "⚡️ Электро",
        "ask_year": "📅 Введите год выпуска (например: <code>2023</code>):",
        "bad_year": "❗️ Введите правильный год (например: 2022).",
        "ask_cc": "🔧 Введите объём двигателя в см³ (например: <code>1600</code>):",
        "bad_cc": "❗️ Введите объём двигателя числом (500 – 10000).",
        "ask_price": "💵 Введите цену авто в долларах США (например: <code>15000</code>):",
        "bad_num": "❗️ Введите число (например: 15000).",
        "ask_delivery": "🚚 Стоимость доставки ($)? Если не знаете, нажмите «Пропустить».",
        "cancelled": "Отменено.",
        "too_old": "⛔️ <b>Внимание:</b> ввоз бензиновых и дизельных авто старше {max} лет в Узбекистан запрещён (возраст авто: {age} лет). Расчёт только для информации.\n\n",
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
            "ℹ️ <b>Как считается растаможка</b>\n\n"
            "• Пошлина: до 1 года — 15% + $1/см³; 1–3 года — 30% + $2.5/см³; старше 3 лет — 40% + $3/см³\n"
            "• Электромобили и последовательные гибриды освобождены от пошлины\n"
            "• НДС: 12% (стоимость + пошлина)\n"
            "• Утильсбор: в БРВ, зависит от объёма двигателя и возраста\n"
            "• 1 БРВ = {brv} сум\n"
            "• Бензин/дизель: запрещены авто старше {max} лет, ниже Euro-5 и праворульные\n\n"
            "Курс — Центральный банк Узбекистана (cbu.uz)."
        ),
        # ---------- Логистика / валюта / поддержка ----------
        "btn_logistics": "🚛 Международная логистика",
        "btn_currency": "💱 Курс валют",
        "btn_declarant": "👨‍💼 Услуги декларанта",
        "staff_title": "👨‍💼 <b>Услуги декларанта</b>\n\nВыберите нужного сотрудника. Нажмите 📞, чтобы получить его номер.",
        "staff_role": {
            "declarant": "🧾 Декларанты",
            "logistics": "🚛 Логистика",
            "manager": "💼 Менеджеры",
        },
        "btn_support": "📞 Связаться с менеджером",
        "support": (
            "📞 <b>Связаться с менеджером</b>\n\n"
            "Если есть вопросы, напишите нашему менеджеру:\n\n"
            "{admins}\n"
            "📞 Телефон: {phone}"
        ),
        "support_btn_write": "✍️ Написать:",
        # ---------- Курс валют ----------
        "cur_title": "💱 <b>Курсы валют</b> ({date})",
        "cur_sum": "сум",
        "cur_source": "<i>Источник: Центральный банк Узбекистана (cbu.uz). ▲▼ — изменение за день.</i>",
        "cur_btn_convert": "🧮 Перевести в сумы",
        "cur_btn_refresh": "🔄 Обновить",
        "cur_refreshed": "Курсы обновлены",
        "cur_pick": "🧮 Какую валюту перевести в сумы?",
        "cur_ask_amount": "✍️ Введите сумму в {ccy} (например: <code>1000</code>):",
        "cur_bad_amount": "❗️ Введите сумму числом (например: 1500).",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} сум</b>\n\nКурс: 1 {ccy} = {rate} сум ({date}, {src})",
        "cur_source_manual": "<i>Источник: официальный курс Центрального банка Узбекистана (cbu.uz).</i>",
        "cur_source_alt": "<i>Сайт ЦБ не ответил, показан рыночный курс (open.er-api.com). Он может немного отличаться от официального.</i>",
        "cur_error": "⚠️ Сейчас не удалось получить курсы. Попробуйте чуть позже.",
        "lg_intro": "🚚 <b>Заявка на перевозку груза</b>\n\nОтветьте на несколько вопросов, и наш оператор свяжется с вами.",
        "lg_ask_origin": "📍 <b>Откуда забрать груз?</b>\n\nНапишите адрес или нажмите «📍 Отправить геолокацию».",
        "lg_ask_destination": "🏁 <b>Куда доставить груз?</b>\n\nНапишите адрес или нажмите «📍 Отправить геолокацию».",
        "lg_btn_location": "📍 Отправить геолокацию",
        "lg_bad_place": "❗️ Напишите адрес текстом или отправьте геолокацию.",
        "lg_ask_cargo": "📦 <b>Выберите тип груза:</b>",
        "lg_ask_cargo_other": "📦 Напишите тип груза (например: <code>автозапчасти</code>):",
        "lg_ask_weight": "⚖️ <b>Примерный вес груза:</b>",
        "lg_ask_volume": "📐 <b>Примерный объём груза:</b>",
        "lg_ask_ready": "⏰ <b>Когда груз будет готов?</b>",
        "lg_ask_ready_other": "📅 Напишите дату (например: <code>15 ноября</code>):",
        "lg_ask_phone": "📱 <b>Ваш номер телефона</b>\n\nНажмите «📱 Отправить номер» или напишите номер (например: <code>+998901234567</code>).",
        "lg_btn_phone": "📱 Отправить номер",
        "lg_bad_phone": "❗️ Введите правильный номер (например: +998901234567) или нажмите кнопку.",
        "lg_use_buttons": "👆 Выберите один из вариантов выше.",
        "lg_confirm": "📋 <b>Ваша заявка:</b>\n\n{summary}\n\n<b>Всё верно?</b>",
        "lg_btn_confirm": "✅ Подтвердить",
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
            "days": "Через 2–3 дня",
            "other": "📅 Другая дата",
        },
        # ---------- Сертификат ----------
        "btn_cert": "📑 Сертификация",
        "ct_intro": "📋 <b>Нужен ли сертификат?</b>\n\nОтветьте на несколько вопросов о товаре. Наш специалист проверит и пришлёт ответ сюда.",
        "ct_ask_product": "📦 <b>Название и описание товара</b>\n\nНапример: <code>детская игрушка, пластик, от 3 лет</code>",
        "ct_ask_code": "🔢 <b>Код ТН ВЭД</b> (если знаете)\n\nЕсли не знаете, нажмите «Пропустить».",
        "ct_ask_country": "🌍 <b>Из какой страны везёте товар?</b>",
        "ct_ask_purpose": "🎯 <b>Для чего ввозится товар?</b>",
        "ct_ask_file": "📎 <b>Фото товара или документ</b> (инвойс, этикетка)\n\nОтправьте фото или файл. Если нет, нажмите «Пропустить».",
        "ct_bad_text": "❗️ Напишите текстом.",
        "ct_bad_file": "❗️ Отправьте фото или файл либо нажмите «Пропустить».",
        "ct_confirm": "📋 <b>Ваша заявка:</b>\n\n{summary}\n\n<b>Всё верно?</b>",
        "ct_thanks": "✅ <b>Заявка принята!</b>\n\nНомер заявки: <b>#{no}</b>\nНаш специалист пришлёт ответ сюда.",
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
        "btn_trade": "📦 Импорт / Экспорт",
        "tr_intro": "🌍 <b>Заказ на импорт / экспорт</b>\n\nОтветьте на несколько вопросов, и наш менеджер свяжется с вами.\n\n❗️ Заказ принимается только с <b>номером телефона</b>.",
        "tr_ask_direction": "🔀 <b>Какая услуга нужна?</b>",
        "tr_ask_product": "📦 <b>Название товара</b>\n\nНапример: <code>бытовая техника, 2 контейнера</code>",
        "tr_ask_country_import": "🌍 <b>Из какой страны ввозится товар?</b>",
        "tr_ask_country_export": "🌍 <b>В какую страну вывозится товар?</b>",
        "tr_ask_volume": "⚖️ <b>Примерный объём или вес</b>\n\nНапример: <code>20 тонн</code>, <code>1 фура</code>. Если не знаете, нажмите «Пропустить».",
        "tr_ask_name": "👤 <b>Ваше имя или название компании</b>",
        "tr_ask_phone": "📱 <b>Ваш номер телефона (обязательно)</b>\n\nНажмите «📱 Отправить номер» или напишите номер (например: <code>+998901234567</code>).",
        "tr_bad_phone": "❗️ Номер телефона обязателен. Введите правильный номер (например: +998901234567) или нажмите «📱 Отправить номер».",
        "tr_confirm": "🌍 <b>Ваш заказ:</b>\n\n{summary}\n\n<b>Всё верно?</b>",
        "tr_thanks": "✅ <b>Заказ принят!</b>\n\nНомер заказа: <b>#{no}</b>\nНаш менеджер скоро свяжется с вами.",
        "tr_field": {
            "direction": "🔀 Услуга",
            "product": "📦 Товар",
            "country": "🌍 Страна",
            "volume": "⚖️ Объём",
            "name": "👤 Имя / компания",
            "phone": "📱 Телефон",
        },
        "tr_direction": {
            "import": "📥 Импорт",
            "export": "📤 Экспорт",
        },
    },
    "en": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "Hello! Welcome to the DCG Cargo bot! 🚚\n\nLogistics, exchange rates and car customs calculator for Uzbekistan.",
        "bot_short_description": "Official DCG Cargo bot 🚚",
        "welcome": "👋 <b>Hello!</b>\n\n🚚 Welcome to the <b>DCG Cargo</b> bot!\n\nChoose a section below 👇",
        "btn_calc": "💰 Customs calculator",
        "btn_info": "ℹ️ Info",
        "btn_lang": "🌐 Language",
        "btn_cancel": "❌ Cancel",
        "btn_skip": "⏭ Skip",
        "ask_fuel": "⛽️ Choose the fuel type:",
        "fuel_ice": "⛽️ Petrol / Diesel",
        "fuel_hybrid": "🔋 Hybrid",
        "fuel_serial": "🔌 Series hybrid (EREV)",
        "fuel_ev": "⚡️ Electric",
        "ask_year": "📅 Enter the year of manufacture (e.g. <code>2023</code>):",
        "bad_year": "❗️ Enter a valid year (e.g. 2022).",
        "ask_cc": "🔧 Enter the engine size in cm³ (e.g. <code>1600</code>):",
        "bad_cc": "❗️ Enter the engine size as a number (500 – 10000).",
        "ask_price": "💵 Enter the car price in US dollars (e.g. <code>15000</code>):",
        "bad_num": "❗️ Enter a number (e.g. 15000).",
        "ask_delivery": "🚚 Delivery cost ($)? If you don't know, tap «Skip».",
        "cancelled": "Cancelled.",
        "too_old": "⛔️ <b>Note:</b> petrol/diesel cars older than {max} years cannot be imported into Uzbekistan (car age: {age} years). This calculation is for information only.\n\n",
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
            "⚠️ <i>This is an estimate. Customs sets the exact amount.</i>"
        ),
        "cc_line": "🔧 Engine: {cc} cm³\n",
        "info": (
            "ℹ️ <b>How the calculation works</b>\n\n"
            "• Customs duty: up to 1 year — 15% + $1/cm³; 1–3 years — 30% + $2.5/cm³; over 3 years — 40% + $3/cm³\n"
            "• Electric cars and series hybrids are duty-free\n"
            "• VAT: 12% (value + duty)\n"
            "• Recycling fee: in BCV, based on engine size and age\n"
            "• 1 BCV (base calculation value) = {brv} UZS\n"
            "• Petrol/diesel: cars older than {max} years, below Euro-5 or right-hand drive are banned\n\n"
            "Exchange rate: Central Bank of Uzbekistan (cbu.uz)."
        ),
        # ---------- Logistics / currency / support ----------
        "btn_logistics": "🚛 International logistics",
        "btn_currency": "💱 Exchange rates",
        "btn_declarant": "👨‍💼 Customs broker",
        "staff_title": "👨‍💼 <b>Customs broker services</b>\n\nChoose the person you need. Tap 📞 to get their number.",
        "staff_role": {
            "declarant": "🧾 Customs brokers",
            "logistics": "🚛 Logistics",
            "manager": "💼 Managers",
        },
        "btn_support": "📞 Contact a manager",
        "support": (
            "📞 <b>Contact a manager</b>\n\n"
            "If you have questions, message our manager:\n\n"
            "{admins}\n"
            "📞 Phone: {phone}"
        ),
        "support_btn_write": "✍️ Message:",
        # ---------- Currency rates ----------
        "cur_title": "💱 <b>Exchange rates</b> ({date})",
        "cur_sum": "UZS",
        "cur_source": "<i>Source: Central Bank of Uzbekistan (cbu.uz). ▲▼ — change since yesterday.</i>",
        "cur_btn_convert": "🧮 Convert to UZS",
        "cur_btn_refresh": "🔄 Refresh",
        "cur_refreshed": "Rates updated",
        "cur_pick": "🧮 Which currency should we convert to UZS?",
        "cur_ask_amount": "✍️ Enter the amount in {ccy} (e.g. <code>1000</code>):",
        "cur_bad_amount": "❗️ Enter the amount as a number (e.g. 1500).",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} UZS</b>\n\nRate: 1 {ccy} = {rate} UZS ({date}, {src})",
        "cur_source_manual": "<i>Source: official rate of the Central Bank of Uzbekistan (cbu.uz).</i>",
        "cur_source_alt": "<i>The Central Bank website did not respond, so the market rate is shown (open.er-api.com). It may differ slightly from the official rate.</i>",
        "cur_error": "⚠️ Couldn't get the rates right now. Please try again later.",
        "lg_intro": "🚚 <b>Cargo transport request</b>\n\nAnswer a few questions and our operator will contact you.",
        "lg_ask_origin": "📍 <b>Where should we pick up the cargo?</b>\n\nType the address or tap «📍 Send location».",
        "lg_ask_destination": "🏁 <b>Where should we deliver the cargo?</b>\n\nType the address or tap «📍 Send location».",
        "lg_btn_location": "📍 Send location",
        "lg_bad_place": "❗️ Type the address or send a location.",
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
        "lg_btn_confirm": "✅ Confirm",
        "lg_btn_edit": "✏️ Edit",
        "lg_btn_drop": "❌ Cancel",
        "lg_btn_back": "⬅️ Back",
        "lg_edit_which": "What would you like to change?",
        "lg_thanks": "✅ <b>Request received!</b>\n\nRequest number: <b>#{no}</b>\nOur operator will contact you soon.",
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
            "unknown": "🤷 Not sure",
        },
        "lg_ready": {
            "now": "✅ Ready now",
            "today": "Today",
            "tomorrow": "Tomorrow",
            "days": "In 2–3 days",
            "other": "📅 Other date",
        },
        # ---------- Certificate ----------
        "btn_cert": "📑 Certification",
        "ct_intro": "📋 <b>Do you need a certificate?</b>\n\nAnswer a few questions about your goods. Our specialist will check and reply here.",
        "ct_ask_product": "📦 <b>Product name and description</b>\n\nFor example: <code>children's toy, plastic, 3+ years</code>",
        "ct_ask_code": "🔢 <b>HS code</b> (if you know it)\n\nIf not, tap «Skip».",
        "ct_ask_country": "🌍 <b>Which country are the goods coming from?</b>",
        "ct_ask_purpose": "🎯 <b>Why are the goods being imported?</b>",
        "ct_ask_file": "📎 <b>Product photo or document</b> (invoice, label)\n\nSend a photo or file. If you don't have one, tap «Skip».",
        "ct_bad_text": "❗️ Please send it as text.",
        "ct_bad_file": "❗️ Send a photo or file, or tap «Skip».",
        "ct_confirm": "📋 <b>Your request:</b>\n\n{summary}\n\n<b>Is everything correct?</b>",
        "ct_thanks": "✅ <b>Request received!</b>\n\nRequest number: <b>#{no}</b>\nOur specialist will reply here.",
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
        "btn_trade": "📦 Import / Export",
        "tr_intro": "🌍 <b>Import / export order</b>\n\nAnswer a few questions and our manager will contact you.\n\n❗️ Orders are accepted only with a <b>phone number</b>.",
        "tr_ask_direction": "🔀 <b>Which service do you need?</b>",
        "tr_ask_product": "📦 <b>Product name</b>\n\nFor example: <code>home appliances, 2 containers</code>",
        "tr_ask_country_import": "🌍 <b>Which country are the goods imported from?</b>",
        "tr_ask_country_export": "🌍 <b>Which country are the goods exported to?</b>",
        "tr_ask_volume": "⚖️ <b>Approximate volume or weight</b>\n\nFor example: <code>20 tons</code>, <code>1 truck</code>. If you don't know, tap «Skip».",
        "tr_ask_name": "👤 <b>Your name or company name</b>",
        "tr_ask_phone": "📱 <b>Your phone number (required)</b>\n\nTap «📱 Send number» or type your number (e.g. <code>+998901234567</code>).",
        "tr_bad_phone": "❗️ A phone number is required. Enter a valid number (e.g. +998901234567) or tap «📱 Send number».",
        "tr_confirm": "🌍 <b>Your order:</b>\n\n{summary}\n\n<b>Is everything correct?</b>",
        "tr_thanks": "✅ <b>Order received!</b>\n\nOrder number: <b>#{no}</b>\nOur manager will contact you soon.",
        "tr_field": {
            "direction": "🔀 Service",
            "product": "📦 Product",
            "country": "🌍 Country",
            "volume": "⚖️ Volume",
            "name": "👤 Name / company",
            "phone": "📱 Phone",
        },
        "tr_direction": {
            "import": "📥 Import",
            "export": "📤 Export",
        },
    },
    "zh": {
        "choose_lang": CHOOSE_LANG,
        "bot_description": "您好！欢迎使用 DCG Cargo 机器人！🚚\n\n物流服务、汇率查询及乌兹别克斯坦汽车清关费用计算。",
        "bot_short_description": "DCG Cargo 官方机器人 🚚",
        "welcome": "👋 <b>您好！</b>\n\n🚚 欢迎使用 <b>DCG Cargo</b> 机器人！\n\n请在下方选择所需服务 👇",
        "btn_calc": "💰 清关计算器",
        "btn_info": "ℹ️ 说明",
        "btn_lang": "🌐 语言",
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
        "ask_price": "💵 请输入车价，单位美元（例如：<code>15000</code>）：",
        "bad_num": "❗️ 请输入数字（例如：15000）。",
        "ask_delivery": "🚚 运费是多少（$）？如不清楚，请点击「跳过」。",
        "cancelled": "已取消。",
        "too_old": "⛔️ <b>注意：</b>车龄超过 {max} 年的汽油/柴油车禁止进口到乌兹别克斯坦（该车车龄：{age} 年）。以下计算仅供参考。\n\n",
        "result": (
            "📊 <b>计算结果</b>\n\n"
            "⛽️ 燃料：{fuel}\n"
            "📅 年份：{year}（{age} 年）\n"
            "{cc_line}"
            "💵 车价：${price}\n"
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
            "• 汽油/柴油车：禁止进口车龄超过 {max} 年、低于欧5排放标准或右舵的车辆\n\n"
            "汇率来源：乌兹别克斯坦中央银行（cbu.uz）。"
        ),
        # ---------- 物流 / 汇率 / 客服 ----------
        "btn_logistics": "🚛 国际物流",
        "btn_currency": "💱 汇率",
        "btn_declarant": "👨‍💼 报关员服务",
        "staff_title": "👨‍💼 <b>报关员服务</b>\n\n请选择所需的工作人员，点击 📞 获取其电话号码。",
        "staff_role": {
            "declarant": "🧾 报关员",
            "logistics": "🚛 物流",
            "manager": "💼 经理",
        },
        "btn_support": "📞 联系经理",
        "support": (
            "📞 <b>联系经理</b>\n\n"
            "如有问题，请联系我们的经理：\n\n"
            "{admins}\n"
            "📞 电话：{phone}"
        ),
        "support_btn_write": "✍️ 联系：",
        # ---------- 汇率 ----------
        "cur_title": "💱 <b>汇率</b>（{date}）",
        "cur_sum": "苏姆",
        "cur_source": "<i>来源：乌兹别克斯坦中央银行（cbu.uz）。▲▼ — 与昨日相比。</i>",
        "cur_btn_convert": "🧮 换算成苏姆",
        "cur_btn_refresh": "🔄 刷新",
        "cur_refreshed": "汇率已更新",
        "cur_pick": "🧮 请选择要换算成苏姆的货币：",
        "cur_ask_amount": "✍️ 请输入 {ccy} 金额（例如：<code>1000</code>）：",
        "cur_bad_amount": "❗️ 请用数字输入金额（例如：1500）。",
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} 苏姆</b>\n\n汇率：1 {ccy} = {rate} 苏姆（{date}，{src}）",
        "cur_source_manual": "<i>来源：乌兹别克斯坦中央银行（cbu.uz）官方汇率。</i>",
        "cur_source_alt": "<i>中央银行网站未响应，当前显示市场汇率（open.er-api.com），可能与官方汇率略有差异。</i>",
        "cur_error": "⚠️ 暂时无法获取汇率，请稍后再试。",
        "lg_intro": "🚚 <b>货运下单</b>\n\n请回答几个问题，我们的客服会尽快与您联系。",
        "lg_ask_origin": "📍 <b>在哪里提货？</b>\n\n请输入地址或点击「📍 发送位置」。",
        "lg_ask_destination": "🏁 <b>货物送到哪里？</b>\n\n请输入地址或点击「📍 发送位置」。",
        "lg_btn_location": "📍 发送位置",
        "lg_bad_place": "❗️ 请输入地址或发送位置。",
        "lg_ask_cargo": "📦 <b>请选择货物类型：</b>",
        "lg_ask_cargo_other": "📦 请输入货物类型（例如：<code>汽车配件</code>）：",
        "lg_ask_weight": "⚖️ <b>货物大概重量：</b>",
        "lg_ask_volume": "📐 <b>货物大概体积：</b>",
        "lg_ask_ready": "⏰ <b>货物什么时候备好？</b>",
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
        "btn_cert": "📑 认证",
        "ct_intro": "📋 <b>是否需要证书？</b>\n\n请回答几个关于货物的问题，专家核实后会在这里回复您。",
        "ct_ask_product": "📦 <b>商品名称和描述</b>\n\n例如：<code>儿童玩具，塑料，3岁以上</code>",
        "ct_ask_code": "🔢 <b>海关编码 (HS)</b>（如果知道）\n\n不知道请点击「跳过」。",
        "ct_ask_country": "🌍 <b>货物从哪个国家运来？</b>",
        "ct_ask_purpose": "🎯 <b>进口货物的用途是什么？</b>",
        "ct_ask_file": "📎 <b>商品照片或文件</b>（发票、标签）\n\n请发送照片或文件。没有请点击「跳过」。",
        "ct_bad_text": "❗️ 请用文字输入。",
        "ct_bad_file": "❗️ 请发送照片或文件，或点击「跳过」。",
        "ct_confirm": "📋 <b>您的申请：</b>\n\n{summary}\n\n<b>信息是否正确？</b>",
        "ct_thanks": "✅ <b>申请已收到！</b>\n\n申请编号：<b>#{no}</b>\n专家会在这里回复您。",
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
        "btn_trade": "📦 进出口",
        "tr_intro": "🌍 <b>进出口订单</b>\n\n请回答几个问题，我们的经理会与您联系。\n\n❗️ 下单必须留下<b>电话号码</b>。",
        "tr_ask_direction": "🔀 <b>您需要哪项服务？</b>",
        "tr_ask_product": "📦 <b>商品名称</b>\n\n例如：<code>家用电器，2个集装箱</code>",
        "tr_ask_country_import": "🌍 <b>货物从哪个国家进口？</b>",
        "tr_ask_country_export": "🌍 <b>货物出口到哪个国家？</b>",
        "tr_ask_volume": "⚖️ <b>大约体积或重量</b>\n\n例如：<code>20吨</code>、<code>1辆货车</code>。不知道请点击「跳过」。",
        "tr_ask_name": "👤 <b>您的姓名或公司名称</b>",
        "tr_ask_phone": "📱 <b>您的电话号码（必填）</b>\n\n请点击「📱 发送号码」或直接输入（例如：<code>+998901234567</code>）。",
        "tr_bad_phone": "❗️ 电话号码为必填项。请输入正确的号码（例如：+998901234567）或点击「📱 发送号码」。",
        "tr_confirm": "🌍 <b>您的订单：</b>\n\n{summary}\n\n<b>信息是否正确？</b>",
        "tr_thanks": "✅ <b>订单已收到！</b>\n\n订单号：<b>#{no}</b>\n我们的经理会尽快与您联系。",
        "tr_field": {
            "direction": "🔀 服务",
            "product": "📦 商品",
            "country": "🌍 国家",
            "volume": "⚖️ 体积",
            "name": "👤 姓名 / 公司",
            "phone": "📱 电话",
        },
        "tr_direction": {
            "import": "📥 进口",
            "export": "📤 出口",
        },
    },
}

# Eski tugma nomlari: foydalanuvchida eski klaviatura qolgan boʻlsa ham tugmalar ishlayveradi
OLD_BTN = {
    "btn_calc": ["🚗 Rastamojkani hisoblash", "🚗 Рассчитать растаможку",
                 "🚗 Car customs calculator", "🚗 汽车清关费用计算"],
    "btn_info": ["ℹ️ Ma'lumot", "ℹ️ Информация"],
    "btn_lang": ["🌐 Tilni o'zgartirish", "🌐 Сменить язык", "🌐 Change language", "🌐 切换语言"],
    "btn_support": ["🆘 Qo'llab-quvvatlash"],
    "btn_currency": ["💱 Currency rates"],
    "btn_cert": ["📋 Sertifikat kerakmi?", "📋 Нужен сертификат?",
                 "📋 Need a certificate?", "📋 需要证书吗？"],
    "btn_trade": ["🌍 Import / Eksport zakaz", "🌍 Заказ импорт / экспорт",
                  "🌍 Import / Export order", "🌍 进出口订单",
                  "🌍 Import / Eksport", "🌍 Импорт / Экспорт", "🌍 Import / Export", "🌍 进出口"],
    "btn_logistics": ["🚚 Logistika", "🚚 Логистика", "🚚 Logistics", "🚚 物流"],
}
OLD_BTN["btn_calc"] += ["🚗 Bojxona hisobi", "🚗 Растаможка авто", "🚗 Car customs", "🚗 汽车清关"]
OLD_BTN["btn_cert"] += ["📋 Sertifikat", "📋 Сертификат", "📋 Certificate", "📋 证书"]
OLD_BTN["btn_support"] += ["🆘 Yordam", "🆘 Поддержка", "🆘 Support", "🆘 客服"]
