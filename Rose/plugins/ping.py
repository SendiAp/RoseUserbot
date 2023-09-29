from .. import *
from pyrogram import Client
import time
from datetime import datetime

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

@app.on_message(commandx(["ping"]) & SUDOERS)
async def alive_check(client, message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    m = await eor(message, "**🤖 Pong !**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await m.edit(f"**🌹 Rose Ping 🌹**\n❊ **Ping:**\n`{ms}` ms\n❊ **Uptime:**\n{uptime}\n**✦҈͜͡➳ My Name:** {client.me.mention}")


__NAME__ = "ping"
__MENU__ = f"""
**🥀 Periksa server bot pengguna.

Latensi Ping ⭐
**Example:** `.ping`
"""
