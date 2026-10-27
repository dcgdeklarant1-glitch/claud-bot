"""
Bojxona stavkalari (Растаможка ставки).
Qonun o'zgarsa, faqat shu faylni tahrirlang.

Manbalar (2026): tezmotors.uz/ru/calculator, auto.ustabor.uz, buxgalter.uz (BHM).
DIQQAT: stavkalar taxminiy — rasmiy qiymatlarni customs.uz da tekshiring.
"""

# Bazaviy hisoblash miqdori (BHM / БРВ), so'm — 2026-yil 1-sentabrdan
BRV = 440_000

# USD kursi topilmasa ishlatiladigan zaxira kurs (so'm)
FALLBACK_USD_RATE = 12_000

# QQS (НДС)
VAT_RATE = 0.12

# Bojxona rasmiylashtiruv yig'imi (BHM da)
CLEARANCE_FEE_BRV = 2.5

# Benzin/dizel uchun maksimal yosh (yildan katta bo'lsa olib kirish taqiqlangan)
MAX_AGE_ICE = 7

# Bojxona boji: yosh toifasi -> (foiz, $ / sm³)
# "new" = 1 yilgacha, "mid" = 1–3 yil, "old" = 3 yildan katta
DUTY = {
    "new": (0.15, 1.0),
    "mid": (0.30, 2.5),
    "old": (0.40, 3.0),
}

# Utilizatsiya yig'imi (BHM da): (dvigatel hajmi chegarasi sm³, 3 yilgacha, 3 yildan katta)
UTIL_ICE = [
    (2000, 120, 270),
    (3000, 180, 330),
    (10**9, 300, 450),
]
# Elektromobil va ketma-ket (seriyali) gibrid
UTIL_EV = (120, 210)

# Bojdan ozod yoqilg'i turlari (2030-yilgacha imtiyoz)
DUTY_FREE_FUELS = {"ev", "serial"}
