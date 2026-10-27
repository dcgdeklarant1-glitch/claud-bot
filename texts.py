"""Bot matnlari: o'zbek (uz) va rus (ru)."""

T = {
    "uz": {
        "choose_lang": "🌐 Tilni tanlang / Выберите язык:",
        "welcome": "👋 Assalomu alaykum!\n\n🚗 <b>Avto Kalkulyator</b> — O'zbekistonga avtomobil olib kirishda bojxona to'lovlarini (rastamojka) hisoblab beradi.\n\nQuyidagi tugmani bosing 👇",
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
        # ---------- Xizmatlar / logistika ----------
        "btn_services": "🛎 Xizmatlar",
        "svc_menu": "🛎 <b>Xizmatlar</b>\n\nKerakli xizmatni tanlang 👇",
        "svc_logistics": "🚚 Logistika (yuk tashish)",
        "svc_currency": "💱 Valyuta kursi",
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
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} so'm</b>\n\nKurs: 1 {ccy} = {rate} so'm ({date}, cbu.uz)",
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
    },
    "ru": {
        "choose_lang": "🌐 Tilni tanlang / Выберите язык:",
        "welcome": "👋 Здравствуйте!\n\n🚗 <b>Авто Калькулятор</b> — рассчитает таможенные платежи (растаможку) при ввозе автомобиля в Узбекистан.\n\nНажмите кнопку ниже 👇",
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
        # ---------- Услуги / логистика ----------
        "btn_services": "🛎 Услуги",
        "svc_menu": "🛎 <b>Услуги</b>\n\nВыберите нужную услугу 👇",
        "svc_logistics": "🚚 Логистика (грузоперевозки)",
        "svc_currency": "💱 Курс валют",
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
        "cur_result": "{flag} <b>{amount} {ccy} = {uzs} сум</b>\n\nКурс: 1 {ccy} = {rate} сум ({date}, cbu.uz)",
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
    },
}
