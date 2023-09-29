from .. import *
import time 
import random 
import asyncio
from pyrogram import Client
from pyrogram import filters, __version__ as pyrover, enums

StartTime = time.time()

async def alive():
    rosex = "v2.0.1"
    dbhealth = "ᴡᴏʀᴋɪɴɢ"
    uptime = get_readable_time((time.time() - StartTime))
    start_time = time.time()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    
    ALIVE_TEX = " 𝙷𝙴𝚈 , 𝙱𝙰𝙱𝙴 😍 𝙸 𝙰𝙼 𝙰𝙻𝙸𝚅𝙴"
    EMOTES = ["😍", "💀", "😊", "👋", "🎉", "🔥", "🌟", "💫", "🚀", "🤖", "👻", "👾", "🧡", "🌹"]

    photo_url = "https://te.legra.ph/file/4489fb9f5bccfe210def1.jpg"
    
    ALIVE_TEXT = f"""{ALIVE_TEX}

ㅤ╔══════💫✨💫═════╗
¹┃ㅤ{random.choice(EMOTES)} s ᴛ ᴀ ᴛ ᴜ s ➫ {dbhealth}
²┃ㅤ{random.choice(EMOTES)} ᴋᴀᴛsᴜᴋɪ   ʙ ᴏ ᴛ ➫ {rosex}
³┃ㅤ{random.choice(EMOTES)} ᴜ ᴘ ᴛ ɪ ᴍ ᴇ ➫ {uptime}
⁴┃ㅤ{random.choice(EMOTES)} ᴘ ɪ ɴ ɢ ➫ {ping_time} ms
⁵┃ㅤ{random.choice(EMOTES)} ᴘ ʏ ᴛ ʜ ᴏ ɴ ➫ {pyrover}
ㅤ╚══════💫✨💫═════╝
ㅤ╔═════🌹🌹🌹🌹═════╗
⁶┃ {random.choice(EMOTES)} s ᴇ ɴ s ᴇ ɪ ➫ {client.me.mention}
ㅤ╚═════🌹🌹🌹🌹═════╝"""

    return ALIVE_TEXT, photo_url


__NAME__ = "alive"
__MENU__ = f"""
**🥀 Periksa Userbot Berfungsi
Atau tidak...**

**Example:** `.alive`
"""
