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


@app.on_message(commandx(["qaudio"]) & SUDOERS)
async def quran_audio(client: Client, message: Message):
    prik = await message.edit("`Processing . . .`")
    link = get_arg(message)
    if not link:
       return await message.edit("**Contoh 1**")
    bot = "AlQuran_audio_bot"
    if link:
        try:
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await tuyul.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(10)
            await tuyul.delete()
    async for quran in client.search_messages(
        bot, filter=enums.MessagesFilter.AUDIO, limit=1
    ):
        await asyncio.gather(
            prik.delete(),
            client.send_audio(
                message.chat.id,
                quran.audio.file_path,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)
    

@app.on_message(commandx(["quran"]) & SUDOERS)
async def quran_bot(client: Client, message: Message):
    args = get_arg(message)
    if not args:
        return await message.edit("**Contoh 1:3**")
    await client.unblock_user("AlFurqanRobot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=await client.resolve_peer("AlFurqanRobot"),
            peer=await client.resolve_peer("AlFurqanRobot"),
            random_id=client.rnd_id(),
            start_param="{args}",
        )
    )
    Ros = await edit_or_reply(message, "`Processing...`")
    await asyncio.sleep(1)
    spambot_msg = response.updates[1].message.id + 1
    status = await app.get_messages(chat_id="AlFurqanRobot", message_ids=spambot_msg)
    await Ros.edit(f"~ {status.text}")
        
