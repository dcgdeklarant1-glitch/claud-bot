"""Ma'lumotlar bazasi: mijozlar, logistika buyurtmalari, import/eksport zakazlari,
sertifikat arizalari, hisob-kitoblar.

Serverda (Render) — Neon Postgres (DATABASE_URL). DATABASE_URL bo'lmasa, lokal SQLite
(bot.db) ishlatiladi: kompyuterda sinash uchun. SQL $1, $2 ... belgilari bilan yoziladi.
"""
import datetime as dt
import json
import logging
import os
import re
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

TZ = dt.timezone(dt.timedelta(hours=5))  # Toshkent vaqti
SQLITE_FILE = Path(__file__).with_name("bot.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,
    username TEXT,
    name TEXT,
    lang TEXT,
    phone TEXT,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS orders (
    no {serial},
    created TEXT NOT NULL,
    user_id BIGINT NOT NULL,
    phone TEXT,
    data TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS certs (
    no {serial},
    created TEXT NOT NULL,
    user_id BIGINT NOT NULL,
    phone TEXT,
    product TEXT,
    data TEXT NOT NULL,
    answer TEXT,
    answered_at TEXT
);
CREATE TABLE IF NOT EXISTS trades (
    no {serial},
    created TEXT NOT NULL,
    user_id BIGINT NOT NULL,
    phone TEXT NOT NULL,
    direction TEXT,
    product TEXT,
    data TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS calcs (
    id {serial},
    created TEXT NOT NULL,
    user_id BIGINT NOT NULL,
    fuel TEXT,
    year INTEGER,
    cc INTEGER,
    price DOUBLE PRECISION,
    delivery DOUBLE PRECISION,
    total_uzs DOUBLE PRECISION,
    total_usd DOUBLE PRECISION
);
"""

_pool = None   # asyncpg pool (Postgres)
_lite = None   # sqlite3 ulanishi (lokal)


def now() -> str:
    return dt.datetime.now(TZ).isoformat(timespec="seconds")

def today() -> str:
    return dt.datetime.now(TZ).date().isoformat()


async def init():
    global _pool, _lite
    url = os.getenv("DATABASE_URL", "").strip()
    if url:
        import asyncpg
        # Neon havolasidagi ?sslmode=...&channel_binding=... ni asyncpg tushunmaydi
        parts = urlsplit(url)
        dsn = urlunsplit(parts._replace(query=""))
        _pool = await asyncpg.create_pool(dsn, ssl="require", min_size=1, max_size=3,
                                          max_inactive_connection_lifetime=60)
        async with _pool.acquire() as con:
            await con.execute(SCHEMA.format(serial="SERIAL PRIMARY KEY"))
        logging.info("Baza: Postgres ulandi")
    else:
        _lite = sqlite3.connect(SQLITE_FILE)
        _lite.row_factory = sqlite3.Row
        _lite.executescript(SCHEMA.format(serial="INTEGER PRIMARY KEY AUTOINCREMENT"))
        logging.warning("DATABASE_URL yo'q: ma'lumotlar lokal %s fayliga yoziladi", SQLITE_FILE.name)


async def _run(kind: str, sql: str, *args):
    if _pool is not None:
        import asyncpg
        lost = (OSError, asyncpg.InterfaceError, asyncpg.PostgresConnectionError)
        for attempt in (1, 2):  # Neon uxlab qolgan ulanishni uzishi mumkin — bir marta qayta urinamiz
            try:
                async with _pool.acquire() as con:
                    if kind == "fetch":
                        return [dict(r) for r in await con.fetch(sql, *args)]
                    if kind == "val":
                        return await con.fetchval(sql, *args)
                    return await con.execute(sql, *args)
            except lost as e:
                if attempt == 2:
                    raise
                logging.warning("Baza ulanishi uzildi, qayta urinilmoqda: %r", e)
    if _lite is None:
        raise RuntimeError("Baza ishga tushirilmagan: avval db.init() ni chaqiring")
    cur = _lite.execute(re.sub(r"\$\d+", "?", sql), args)
    if kind == "fetch":
        return [dict(r) for r in cur.fetchall()]
    if kind == "val":
        row = cur.fetchone()
        _lite.commit()
        return row[0] if row else None
    _lite.commit()

async def fetch(sql: str, *args) -> list[dict]:
    return await _run("fetch", sql, *args)

async def fetchval(sql: str, *args):
    return await _run("val", sql, *args)

async def execute(sql: str, *args):
    return await _run("exec", sql, *args)


# ---------- Mijozlar ----------
async def touch_user(user):
    """Mijozni qo'shadi yoki ismi/username va oxirgi faolligini yangilaydi."""
    t = now()
    await execute(
        "INSERT INTO users (id, username, name, first_seen, last_seen) VALUES ($1, $2, $3, $4, $5) "
        "ON CONFLICT (id) DO UPDATE SET username = EXCLUDED.username, name = EXCLUDED.name, "
        "last_seen = EXCLUDED.last_seen",
        user.id, user.username, user.full_name, t, t)

async def set_lang(user, lang: str):
    await touch_user(user)
    await execute("UPDATE users SET lang = $1 WHERE id = $2", lang, user.id)

async def set_phone(user_id: int, phone: str):
    await execute("UPDATE users SET phone = $1 WHERE id = $2", phone, user_id)

async def user_langs() -> dict:
    rows = await fetch("SELECT id, lang FROM users WHERE lang IS NOT NULL")
    return {str(r["id"]): r["lang"] for r in rows}


# ---------- Logistika buyurtmalari ----------
async def add_order(user, data: dict) -> int:
    await touch_user(user)
    await set_phone(user.id, data.get("phone"))
    return await fetchval(
        "INSERT INTO orders (created, user_id, phone, data) VALUES ($1, $2, $3, $4) RETURNING no",
        now(), user.id, data.get("phone"), json.dumps(data, ensure_ascii=False))


# ---------- Import / eksport zakazlari ----------
async def add_trade(user, data: dict) -> int:
    await touch_user(user)
    await set_phone(user.id, data["phone"])
    return await fetchval(
        "INSERT INTO trades (created, user_id, phone, direction, product, data) "
        "VALUES ($1, $2, $3, $4, $5, $6) RETURNING no",
        now(), user.id, data["phone"], data.get("direction"), data.get("product"),
        json.dumps(data, ensure_ascii=False))


# ---------- Sertifikat arizalari ----------
async def add_cert(user, data: dict) -> int:
    await touch_user(user)
    await set_phone(user.id, data.get("phone"))
    return await fetchval(
        "INSERT INTO certs (created, user_id, phone, product, data) VALUES ($1, $2, $3, $4, $5) RETURNING no",
        now(), user.id, data.get("phone"), data.get("product"), json.dumps(data, ensure_ascii=False))

async def answer_cert(no: int, answer: str):
    """Mutaxassis javobini yozadi; bir nechta javob bo'lsa, oldingilari ham saqlanib qoladi."""
    old = await fetchval("SELECT answer FROM certs WHERE no = $1", no)
    if old:
        answer = f"{old}\n\n{answer}"
    await execute("UPDATE certs SET answer = $1, answered_at = $2 WHERE no = $3", answer, now(), no)


# ---------- Rastamojka hisob-kitoblari ----------
async def add_calc(user, fuel, year, cc, price, delivery, total_uzs, total_usd):
    await touch_user(user)
    await execute(
        "INSERT INTO calcs (created, user_id, fuel, year, cc, price, delivery, total_uzs, total_usd) "
        "VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)",
        now(), user.id, fuel, year, cc, price, delivery, total_uzs, total_usd)
