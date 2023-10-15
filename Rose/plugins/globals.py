"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from pyrogram import Client 
from pyrogram.enums import ChatType
import asyncio
from ..import *
from ..modules.basic import edit_or_reply
from ..modules import get_ub_chats, extract_user, extract_user_and_reason

DEVS = "1307579425"

@app.on_message(commandx(["gban", "ungban"]) & SUDOERS)
async def _(client, message):
    user_id = await extract_user(message)
    rose = await message.reply("<b>Memproses. . .</b>")
    if not user_id:
        return await rose.edit("<b>User tidak ditemukan</b>")
    if user_id == client.me.id:
        return await rose.edit("Tidak bisa Gban diri sendiri.")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await rose.edit(error)
    done = 0
    failed = 0
    text = [
        "<b>💬 Global Banned</b>\n\n<b>✅ Berhasil: {} Chat</b>\n<b>❌ Gagal: {} Chat</b>\n<b>👤 User: <a href='tg://user?id={}'>{} {}</a></b>",
        "<b>💬 Global Unbanned</b>\n\n<b>✅ Berhasil: {} Chat</b>\n<b>❌ Gagal: {} Chat</b>\n<b>👤 User: <a href='tg://user?id={}'>{} {}</a></b>",
    ]
    if message.command[0] == "gban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                if user.id == DEVS:
                    return await rose.edit(
                        "Anda tidak bisa gban dia, karena dia pembuat saya"
                    )
                elif not user.id == DEVS:
                    try:
                        await client.ban_chat_member(chat_id, user.id)
                        done += 1
                        await asyncio.sleep(0.1)
                    except:
                        failed += 1
                        await asyncio.sleep(0.1)
        await rose.delete()
        return await message.reply(
            text[0].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "ungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except:
                    failed += 1
                    await asyncio.sleep(0.1)
        await rose.delete()
        return await message.reply(
            text[1].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "cgban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                if user.id == DEVS:
                    return await rose.edit(
                        "Anda tidak bisa gban dia, karena dia pembuat saya"
                    )
                elif not user.id == DEVS:
                    try:
                        await client.ban_chat_member(chat_id, user.id)
                        done += 1
                        await asyncio.sleep(0.1)
                    except:
                        failed += 1
                        await asyncio.sleep(0.1)
        await rose.delete()
        return await message.reply(
            text[0].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )
    elif message.command[0] == "cungban":
        async for dialog in client.get_dialogs():
            chat_type = dialog.chat.type
            if chat_type in [
                ChatType.GROUP,
                ChatType.SUPERGROUP,
                ChatType.CHANNEL,
            ]:
                chat_id = dialog.chat.id
                try:
                    await client.unban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except:
                    failed += 1
                    await asyncio.sleep(0.1)
        await rose.delete()
        return await message.reply(
            text[1].format(
                done, failed, user.id, user.first_name, (user.last_name or "")
            )
        )


__NAME__ = "globals"
__MENU__ = f"""
✘ **Perintah:** `{cmds}gban` [reply user]
• **Fungsi:** Melakukan Global Banned Ke Semua Grup Dimana anda Sebagai Admin.

✘ **Perintah:** `{cmds}ungban` [reply user] 
• **Fungsi:** Membatalkan global banned.

© Rose Userbot
"""
