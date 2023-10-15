"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from ..modules.tools import get_arg

from ..import *
from ..modules import *

@app.on_message(commandx(["q", "quotly"]) & SUDOERS)
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**Mohon Balas ke Pesan**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("`Making a Quote . . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Gagal Membuat Sticker Quotly**")


__NAME__ = "quotly"
__MENU__ = f"""
✘ **Perintah:** `{cmds}q` or `.quotly`
• **Fungsi:** Membuat pesan menjadi sticker dengan random background.

✘ **Perintah:** `{cmds}q` [warna] or `.quotly`
• **Fungsi:** Membuat pesan menjadi sticker dengan custom warna background yang diberikan.
        
© Rose Userbot
"""
