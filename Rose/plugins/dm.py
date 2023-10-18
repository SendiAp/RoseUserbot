"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from ..modules.tools import get_arg
from .. import *

@app.on_message(commandx(["dm"]) & SUDOERS)
async def dm(coli: Client, memek: Message):
    geez = await memek.reply_text("⚡ Proccessing.....")
    quantity = 1
    inp = memek.text.split(None, 2)[1]
    user = await coli.get_chat(inp)
    spam_text = ' '.join(memek.command[2:])
    quantity = int(quantity)

    if memek.reply_to_message:
        reply_to_id = memek.reply_to_message.message_id
        for _ in range(quantity):
            await geez.edit("Message Sended Successfully 😘")
            await coli.send_message(user.id, spam_text,
                                      reply_to_messsge_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await coli.send_message(user.id, spam_text)
        await geez.edit("Message Sended Successfully 😘")
        await asyncio.sleep(0.15)



@app.on_message(commandx(["copy"]) & SUDOERS)
async def copy_msg(client: Client, message: Message):
    lugay = await message.reply("`Processing...`")
    link = get_arg(message)
    if not link:
        return await lugay.edit(f"<b><code>{message.text}</code> [link_konten_telegram]</b>")
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
        except Exception as error:
            await lugay.edit(error)
        await get.copy(message.chat.id)
        return await lugay.delete()
    else:
        await lugay.edit("`harap berikan link telegram dengan benar.`")


__NAME__ = "directmessage"
__MENU__ = f"""
✘ **Perintah:** `{cmds}dm` [username]
• **Fungsi:** Untuk Mengirim Pesan Tanpa Harus Kedalam Roomchat.

© Rose Userbot
"""
