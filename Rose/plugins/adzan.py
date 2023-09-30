#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Rose | Rose Premium 

import json
import requests
from pyrogram import Client
from pyrogram.types import Message
from ..import *

@app.on_message(commandx(["adzan", "jadwal"]) & SUDOERS)
async def adzan_shalat(client: Client, message: Message):
    LOKASI = message.text.split(" ", 1)[1]
    if not LOKASI:
        await message.reply("<i>Silahkan Masukkan Nama Kota Anda</i>")
        return True
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await message.reply(f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    geezram = f"""
<b>Jadwal Shalat Wilayah {LOKASI}</b>
<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit  :</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh :</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur  :</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar  :</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib :</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya :</b> <code>{result['items'][0]['isha']}</code>
"""
    await message.reply(geezram)


__NAME__ = "adzan"
__MENU__ = f"""
**🥀 Melihat jadwal sholat seluruh kota
biar pada rajin ya sayang sholat nya.**

`.adzan` [Kota] - Menampilkan jadwal adzan yang tersedia dibot.

© Rose Userbot
"""
