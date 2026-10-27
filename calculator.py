"""Rastamojka hisoblash mantiqi."""
from dataclasses import dataclass
import datetime as dt

import rates as R


def age_group(year: int) -> tuple[str, int]:
    age = dt.date.today().year - year
    if age < 1:
        return "new", age
    if age <= 3:
        return "mid", age
    return "old", age


@dataclass
class Result:
    customs_value: float  # $
    duty: float           # $
    vat: float            # $
    util_brv: float
    util_uzs: float
    clearance_uzs: float
    usd_rate: float
    total_uzs: float
    total_usd: float
    age: int
    too_old: bool


def calculate(fuel: str, year: int, cc: int, price: float, delivery: float, usd_rate: float) -> Result:
    group, age = age_group(year)
    value = price + delivery

    if fuel in R.DUTY_FREE_FUELS:
        duty = 0.0
    else:
        pct, per_cc = R.DUTY[group]
        duty = value * pct + cc * per_cc

    vat = (value + duty) * R.VAT_RATE

    up_to_3 = age <= 3
    if fuel in ("ev", "serial"):
        util_brv = R.UTIL_EV[0] if up_to_3 else R.UTIL_EV[1]
    else:
        util_brv = next((a if up_to_3 else b) for lim, a, b in R.UTIL_ICE if cc <= lim)

    util_uzs = util_brv * R.BRV
    clearance_uzs = R.CLEARANCE_FEE_BRV * R.BRV
    total_uzs = (duty + vat) * usd_rate + util_uzs + clearance_uzs
    too_old = fuel not in ("ev",) and age > R.MAX_AGE_ICE

    return Result(value, duty, vat, util_brv, util_uzs, clearance_uzs, usd_rate,
                  total_uzs, total_uzs / usd_rate, age, too_old)
