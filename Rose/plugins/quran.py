import asyncio
import io
import os
import random
import textwrap
import requests
from io import BytesIO
from base64 import b64decode
from pyrogram import Client, errors
from pyrogram.types import Message
from emoji import get_emoji_regexp
from PIL import Image, ImageDraw, ImageFont
from ..modules.basic import edit_or_reply
from ..modules.tools import get_arg
from ..modules import *
from ..import *


@app.on_message(commandx(["quran"]) & SUDOERS)
async def quran(client: Client, message: Message):
    args = get_arg(message)
    if not args:
        return await message.edit("**Contoh 1:3**")
    bot = "AlFurqanRobot"
    if message.reply_to_message:
        await message.edit("`Waiting Proses. . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"{args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.edit("`Sedikit Lagi. . .`")
        await asyncio.sleep(1)
        quran_msg = response.updates[1].message.id + 1
        status = await app.get_messages(chat_id="AlFurqanRobot", message_ids=quran_msg)
        await message.edit(f"{status.text}")


@app.on_message(commandx(["quranbot"]) & SUDOERS)
async def quran_bot(client: Client, message: Message):
    args = get_arg(message)
    if not args:
        return await message.edit("**Contoh 1:3**")
    bot = "AlFurqanRobot"
    await client.unblock_user(bot)
    response = await client.send_message(bot, f"{args}")
    Ros = await edit_or_reply(message, "`Processing...`")
    await asyncio.sleep(1)
    status = await app.get_messages(chat_id=bot)
    await Ros.edit(f"~ {status.text}")
