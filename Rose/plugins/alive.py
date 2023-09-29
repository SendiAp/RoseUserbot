from .. import *
import time 
import random 
import asyncio
from pyrogram import Client
from pyrogram import filters, __version__ as pyrover, enums

async def get_readable_time(seconds: int) -> str:    
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    
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

    photo_url = "https://telegra.ph/file/6cd188eddea9ae8154d1d.jpg"
    
    ALIVE_TEXT = f"""{ALIVE_TEX}

ㅤ╔══════💫✨💫═════╗
¹┃ㅤ{random.choice(EMOTES)} ꜱᴛᴀᴛᴜꜱ ➫ {dbhealth}
²┃ㅤ{random.choice(EMOTES)} ʀᴏꜱᴇ ᴜꜱᴇʀʙᴏᴛ ➫ {rosex}
³┃ㅤ{random.choice(EMOTES)} ᴜᴘᴛɪᴍᴇ ➫ {uptime}
⁴┃ㅤ{random.choice(EMOTES)} ᴘɪɴɢ ➫ {ping_time} ms
⁵┃ㅤ{random.choice(EMOTES)} ᴘʏᴛʜᴏɴ ➫ {pyrover}
ㅤ╚══════💫✨💫═════╝
ㅤ╔═════🌹🌹🌹🌹═════╗
⁶┃ {random.choice(EMOTES)} ꜱᴇɴꜱᴇɪ ➫ {client.me.mention}
ㅤ╚═════🌹🌹🌹🌹═════╝"""

    return ALIVE_TEXT, photo_url


__NAME__ = "alive"
__MENU__ = f"""
**🥀 Periksa Userbot Berfungsi
Atau tidak...**

**Example:** `.alive`
"""
