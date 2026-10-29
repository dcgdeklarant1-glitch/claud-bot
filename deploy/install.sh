#!/usr/bin/env bash
# DCG bot: VPS'ga o'rnatish yoki yangilash (qayta ishga tushirsa — yangilaydi).
#
# Serverdagi saytga tegmaydi:
#   • bot alohida "dcgbot" foydalanuvchisi nomidan, /opt/dcgbot papkasida ishlaydi;
#   • o'zining alohida Python'i bor (tizim Python'i va sayt kutubxonalari o'zgarmaydi);
#   • hech qanday port ochmaydi (Telegram bilan polling orqali ishlaydi, nginx/apache'ga tegmaydi);
#   • xotira va protsessor ulushi cheklangan, sayt sekinlashmaydi.
#
# Ishga tushirish (root bilan):
#   curl -fsSL https://raw.githubusercontent.com/dcgdeklarant1-glitch/claud-bot/main/deploy/install.sh | bash
set -euo pipefail

BOT_USER=dcgbot
HOME_DIR=/opt/dcgbot
APP_DIR=$HOME_DIR/app
VENV=$HOME_DIR/venv
REPO=https://github.com/dcgdeklarant1-glitch/claud-bot.git
SERVICE=/etc/systemd/system/dcgbot.service

say() { printf '\n\033[1;32m==> %s\033[0m\n' "$*"; }

[ "$(id -u)" -eq 0 ] || { echo "Bu skriptni root foydalanuvchisi bilan ishga tushiring."; exit 1; }

say "Kerakli dasturlar (git, curl)"
if ! command -v git >/dev/null || ! command -v curl >/dev/null; then
    if command -v apt-get >/dev/null; then
        apt-get update -qq && apt-get install -y -qq git curl ca-certificates
    elif command -v dnf >/dev/null; then
        dnf install -y -q git curl
    else
        yum install -y -q git curl
    fi
fi

say "Alohida foydalanuvchi: $BOT_USER"
if ! id "$BOT_USER" >/dev/null 2>&1; then
    useradd --system --create-home --home-dir "$HOME_DIR" --shell /usr/sbin/nologin "$BOT_USER"
fi
as_bot() { runuser -u "$BOT_USER" -- env HOME="$HOME_DIR" "$@"; }

say "Bot kodi"
if [ -d "$APP_DIR/.git" ]; then
    as_bot git -C "$APP_DIR" pull --ff-only
else
    as_bot git clone "$REPO" "$APP_DIR"
fi

say "Alohida Python 3.12 va kutubxonalar"
UV=$HOME_DIR/.local/bin/uv
if [ ! -x "$UV" ]; then
    as_bot sh -c "curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=$HOME_DIR/.local/bin INSTALLER_NO_MODIFY_PATH=1 sh"
fi
[ -x "$VENV/bin/python" ] || as_bot "$UV" venv --python 3.12 "$VENV"
as_bot "$UV" pip install --python "$VENV/bin/python" -q -r "$APP_DIR/requirements.txt"

say "Sozlamalar fayli (.env)"
ENV_FILE=$APP_DIR/.env
if [ ! -f "$ENV_FILE" ]; then
    cat > "$ENV_FILE" <<'EOF'
# Render'dagi Environment bo'limidagi qiymatlarni shu yerga qo'ying (= dan keyin, probelsiz)
BOT_TOKEN=
ADMIN_ID=
DATABASE_URL=
EOF
fi
chown "$BOT_USER:$BOT_USER" "$ENV_FILE"
chmod 600 "$ENV_FILE"

say "Avtomatik ishga tushish (systemd)"
cat > "$SERVICE" <<EOF
[Unit]
Description=DCG Telegram bot
After=network-online.target
Wants=network-online.target

[Service]
User=$BOT_USER
WorkingDirectory=$APP_DIR
ExecStart=$VENV/bin/python bot.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1
# Sayt sekinlashmasligi uchun cheklovlar
MemoryMax=400M
CPUQuota=50%
Nice=10

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
systemctl enable dcgbot >/dev/null 2>&1

if grep -qE '^BOT_TOKEN=.+:.+' "$ENV_FILE"; then
    systemctl restart dcgbot
    sleep 5
    systemctl --no-pager --lines=15 status dcgbot || true
    say "Tayyor! Bot ishlayapti. Jurnal: journalctl -u dcgbot -f"
else
    say "Deyarli tayyor. Endi tokenlarni kiriting:"
    echo "    nano $ENV_FILE"
    echo "so'ng botni ishga tushiring:"
    echo "    systemctl restart dcgbot && journalctl -u dcgbot -f"
fi
