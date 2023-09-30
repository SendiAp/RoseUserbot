import asyncio
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.types import Message

from ..import aiosession
from ..modules.basic import edit_or_reply
from ..modules.basic import ReplyCheck

from ..import *

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(commandx(["carbon", "crbn"]) & SUDOERS)
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    Man = await edit_or_reply(message, "`Preparing Carbon . . .`")
    carbon = await make_carbon(text)
    await Man.edit("`Uploading . . .`")
    await asyncio.gather(
        Man.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"**Carbonised by** {client.me.mention}",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()


__NAME__ = "carbon"
__MENU__ = f"""
**🥀 Kalau mau buat carbon tipis² gaskeun
ikuti perintah dibawah ya bawah.**

`.carbon` [reply] - **Carbonisasi teks dengan pengaturan default.**

© Rose Userbot
"""
