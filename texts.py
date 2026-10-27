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
    },
}
