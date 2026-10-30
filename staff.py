"""Xodimlar roʻyxati: «Deklarant xizmati» menyusida mijozga koʻrsatiladi.

Yangi xodim qoʻshish uchun roʻyxatga bitta qator qoʻshing:
    role     — "declarant" (deklarant), "logistics" (logistika) yoki "manager" (menejer)
    name     — xodimning ismi
    phone    — telefon raqami (+998 bilan)
    username — Telegram username (@ belgisisiz); boʻlmasa "" qoldiring
"""

STAFF = [
    {"role": "manager", "name": "DCG menejer", "phone": "+998555001113", "username": "DCG_manager"},
    {"role": "manager", "name": "DCG admin", "phone": "+998555001113", "username": "Dcgadmin2229"},
]

# Menyuda boʻlimlar shu tartibda chiqadi
ROLES = ("declarant", "logistics", "manager")
