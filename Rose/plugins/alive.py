import random 
import asyncio
import os
import time
from platform import python_version
from os import getenv
from datetime import datetime

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from ..modules.vars import Config
from ..modules.vars import all_vars, all_vals
from .ping import StartTime
from ..modules.basic import edit_or_reply
from ..modules.basic import ReplyCheck
from ..modules.tools import convert_to_image
from .ping import get_readable_time
from ..modules.mc import restart
from ..import __version__
from ..import *

EMOTES = ["😍", "💀", "😊", "👋", "🎉", "🔥", "🌟", "💫", "🚀", "🤖", "👻", "👾", "🧡", "🌹", "🩲"]

DANA = getenv("DANA", "085894831504 S.A.P")
SHOPE = getenv("SHOPE", "085894831504 S.A.P")
GOPAY = getenv("GOPAY", "085894831504 S.A.P")
OVO = getenv("OVO", "085894831504 S.A.P")
LINKAJA = getenv("LINKAJA", "085894831504 S.A.P")
BCA = getenv("BCA", "4860428721 DEWI HENDRIANI")
BRI = getenv("BRI", None)
JAGO = getenv("JAGO", "100875241009 D.H")
PERINGATAN = getenv("PERINGATAN", "Kalau lu donasi pahala lu gede")


@app.on_message(commandx(["alive"]) & SUDOERS)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "🌹")
    await asyncio.sleep(2)
    alive_logo = var.ALIVE_LOGO
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    ros = (
        f"**𝙷𝙴𝚈 , 𝙱𝙰𝙱𝙴 {random.choice(EMOTES)} 𝙸 𝙰𝙼 𝙰𝙻𝙸𝚅𝙴!**\n\n"
        f"{random.choice(EMOTES)} <b>Master :</b> {client.me.mention} \n"
        f"{random.choice(EMOTES)} <b>Bot Version :</b> <code>{__version__}</code> \n"
        f"{random.choice(EMOTES)} <b>Python Version :</b> <code>{python_version()}</code> \n"
        f"{random.choice(EMOTES)} <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f"{random.choice(EMOTES)} <b>Bot Ping :</b> <code>{ms}</code> \n"
        f"{random.choice(EMOTES)} <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"**[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/RoseUserbotSupport)** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/RoseUserbotV2)** | **[𝗚𝗶𝘁𝗵𝘂𝗯](https://github.com/SendiAp/RoseUserbot)**"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            client.send_photo(
                message.chat.id,
                alive_logo,
                caption=ros,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(ros, disable_web_page_preview=True)


@app.on_message(commandx(["donasi", "d", "payment", "p"]) & SUDOERS)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "Sedang Mengambil Data Payment...")
    await asyncio.sleep(2)
    dana = DANA
    shope = SHOPE
    gopay = GOPAY 
    linkaja = LINKAJA
    bca = BCA
    bri = BRI
    jago = JAGO
    peringatan = PERINGATAN 
    qris = var.QRIS
    pay = (
        f"𝗤𝗥𝗜𝗦 & 𝗔𝗟𝗟 𝗣𝗔𝗬𝗠𝗘𝗡𝗧\n\n"
        f"🏧 **DANA:** {dana}\n\n"
        f"🏧 **ShopeePay:** {shope}\n\n"
        f"🏧 **Gopay:** {gopay}\n\n"
        f"🏧 **Ovo:** {ovo}\n\n"
        f"🏧 **LinkAja:** {linkaja}\n\n"
        f"🏧 **BCA:** {bca}\n\n"
        f"🏧 **BRI:** {bri}\n\n"
        f"🏧 **BankJago:** {jago}\n\n"
        f"🆘 PERINGATAN BACA!\n"
        f"{peringatan}"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            client.send_photo(
                message.chat.id,
                qris,
                caption=pay,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(pay, disable_web_page_preview=True)
        
