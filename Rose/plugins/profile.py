"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from ..modules.basic import edit_or_reply
from ..modules.basic import ReplyCheck
from ..modules.tools import extract_user

from ..import *

flood = {}

@app.on_message(commandx(["block"]) & SUDOERS)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Ros = await edit_or_reply(message, "`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Berikan User ID/Username atau reply pesan pengguna untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await Ros.edit("anda stress harap segera minum obat.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil Memblokir** {umention}")


@app.on_message(commandx(["unblock"]) & SUDOERS)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Ros = await edit_or_reply(message, "`Processing . . .`")
    if not user_id:
        return await message.edit(
            "Berikan User ID/Username atau reply pesan pengguna untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await Ros.edit("anda stress harap segera minum obat.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil Membuka Blokir** {umention}")


@app.on_message(commandx(["setname"]) & SUDOERS)
async def setname(client: Client, message: Message):
    Ros = await edit_or_reply(message, "`Processing . . .`")
    if len(message.command) == 1:
        return await Ros.edit(
            "Berikan teks untuk ditetapkan sebagai nama telegram anda."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await Ros.edit(f"**Berhasil Mengubah Nama Telegram anda Menjadi** `{name}`")
        except Exception as e:
            await Ros.edit(f"**ERROR:** `{e}`")
    else:
        return await Ros.edit(
            "Berikan teks untuk ditetapkan sebagai nama telegram anda."
        )


@app.on_message(commandx(["setbio"]) & SUDOERS)
async def set_bio(client: Client, message: Message):
    Ros = await edit_or_reply(message, "`Processing . . .`")
    if len(message.command) == 1:
        return await Ros.edit("Berikan teks untuk ditetapkan sebagai bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await Ros.edit(f"**Berhasil Mengubah BIO anda menjadi** `{bio}`")
        except Exception as e:
            await Ros.edit(f"**ERROR:** `{e}`")
    else:
        return await Ros.edit("Berikan teks untuk ditetapkan sebagai bio.")


__NAME__ = "profile"
__MENU__ = f"""
✘ **Perintah:** `.block`
• **Fungsi:** Untuk memblokir pengguna telegram.

✘ **Perintah:** `.unblock`
• **Fungsi:** Untuk membuka pengguna yang anda blokir.

✘ **Perintah:** `.setname`
• **Fungsi:** Untuk Mengganti Nama Telegram.

✘ **Perintah:** `.setbio` 
Untuk Mengganti Bio Telegram.

© Rose Userbot
"""
