import random 
import asyncio
import os
import time
from platform import python_version

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

alive_logo = Config.ALIVE_LOGO

EMOTES = ["😍", "💀", "😊", "👋", "🎉", "🔥", "🌟", "💫", "🚀", "🤖", "👻", "👾", "🧡", "🌹", "🩲"]

@app.on_message(commandx(["alive"]) & SUDOERS)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "🌹")
    await asyncio.sleep(2)
    uptime = await get_readable_time((time.time() - StartTime))
    ros = (
        f"**[Rose-Userbot](https://github.com/SendiAp/RoseUserbot) is Up and Running.**\n\n"
        f"{random.choice(EMOTES)} <b>Master :</b> {client.me.mention} \n"
        f"{random.choice(EMOTES)} <b>Bot Version :</b> <code>{__version__}</code> \n"
        f"{random.choice(EMOTES)} <b>Python Version :</b> <code>{python_version()}</code> \n"
        f"{random.choice(EMOTES)} <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f"{random.choice(EMOTES)} <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/RoseUserbotSupport)** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/RoseUserbotV2)** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})**"
    )
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=ros,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(ros, disable_web_page_preview=True)

