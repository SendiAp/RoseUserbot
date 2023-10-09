import heroku3
import time
import re
import asyncio
import math
import shutil
import sys
import dotenv
import datetime
from ..import *
from ..modules import *
from dotenv import load_dotenv
from os import environ, execle, path
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from itertools import count
from pyrogram import *
from platform import python_version as py
from pyrogram import __version__ as pyro
from pyrogram.types import * 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO


@bot.on_message(filters.command(["start"]) & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 Halo {message.from_user.first_name}!
	@RosePremiumBot adalah bot yang membantu mengubah akun anda jadi menjadi userbot.\n
 👉 Hubungi owner bot ini dan lakukan transaksi untuk mengaktifkan userbot kamu.\n
❓ APA PERINTAHNYA? ❓
Tekan /deploy untuk melihat semua perintah dan cara kerjanya.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
              InlineKeyboardButton(text="🌹 Beli Premium 🌹", callback_data="peringatan_user"),
                ],
                [
                    InlineKeyboardButton(text="🦅 Channel", url="https://t.me/smprojectID"),
                    InlineKeyboardButton(text="🦅 Groups", url="https://t.me/bottycustoree"),
                ],
                [
              InlineKeyboardButton(text="Jumlah Pengguna", callback_data="user_diamond"),
                ],
            ]
        ),
     disable_web_page_preview=True
    )
