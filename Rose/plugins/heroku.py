"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import asyncio
import math
import os
import dotenv
import heroku3
import requests
import urllib3
from ..modules.bc import is_heroku
from ..modules.vars import *
from ..import *
from ..modules.mc import restart

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEROKU_API_KEY = var.HEROKU_API_KEY
HEROKU_APP_NAME = var.HEROKU_APP_NAME

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


@app.on_message(commandx(["getvar"]) & SUDOERS)
async def varget_(client, message):
    usage = f"**Usage:**\n.get_var [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pastikan Heroku API Key, App name sudah benar"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"**Heroku Config:**\n\n**{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await message.reply_text("Var tidak ditemukan")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env tidak ditemukan.")
        output = dotenv.get_key(path, check_var)
        if not output:
            return await message.reply_text("var tidak ditemukan")
        else:
            return await message.reply_text(
                f".env:\n\n**{check_var}:** `{str(output)}`"
            )


@app.on_message(commandx(["delvar"]) & SUDOERS)
async def vardel_(client, message):
    usage = f"**Usage:**\n.delvar [nama var]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pastikan Heroku API Key, App name sudah benar"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            await message.reply_text(
                f"**Heroku Var:**\n\n`{check_var}` Sukses dihapus."
            )
            del heroku_config[check_var]
        else:
            return await message.reply_text(f"Var tidak ditemukan")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env tidak ditemukan.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text(",env var tidak ditemukan")
        else:
            return await message.reply_text(
                f".env Var :\n\n`{check_var}` Berhasil dihapus. ketik {cmds}restart untuk restart bot."
            )


@app.on_message(commandx(["setvar"]) & SUDOERS)
async def setvar(client, message):
    usage = f"**Usage:**\n.setvar [nama var] [isi var]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pastikan Heroku API Key, App name sudah benar"
            )
        heroku_config = happ.config()
        if to_set in heroku_config:
            await message.reply_text(
                f"**Heroku Var diupdate:**\n\n`{to_set}` sukses ter-Update. Bot akan restart."
            )
        else:
            await message.reply_text(
                f"Vars `{to_set}`berhasil dibuat. Bot akan restart."
            )
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            return await message.reply_text(
                f"**.env Var:**\n\n`{to_set}`berhasil diupdate. ketik {cmds}restart untuk merestart bot."
            )
        else:
            return await message.reply_text(
                f"**.env Var:**\n\n`{to_set}`berhasil dibuat. ketik {cmds}restart untuk merestart bot."
            )


@app.on_message(commandx(["usage"]) & SUDOERS)
async def usage_dynos(client, message):
    if is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
    else:
            return await message.reply_text("Hanya untuk Heroku Deployment")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    dyno = await message.reply_text("Memeriksa penggunaan dyno...")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    day = math.floor(hours / 24)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
⚙️ **Dyno Heroku** ⚙️:
➸ Pemakaian Dyno:
•  `{AppHours}`**Jam** `{AppMinutes}`**Menit |**  [`{AppPercentage}`**%**]
➸ Sisa kuota dyno bulan ini:
•  `{hours}`**Jam**  `{minutes}`**Menit |**  [`{percentage}`**%**]
➸ **Sisa Dyno Heroku** `{day}` **Hari Lagi**"""
    return await dyno.edit(text)


__NAME__ = "heroku"
__MENU__ = f"""
✘ **Perintah:** `.setvar` [VAR] [VALUE]
• **Fungsi:** Untuk mengatur variabel config userbot.

✘ **Perintah:** `.delvar` [VAR] 
• **Fungsi:** Untuk menghapus variabel config userbot.

✘ **Perintah:** `.getvar` [VAR] 
• **Fungsi:** Untuk melihat variabel config userbot.

✘ **Perintah:** `.usage`
• **Fungsi:** Untuk mengecheck kouta dyno heroku.

© Rose Userbot
"""
