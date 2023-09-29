import asyncio
import dotenv
from pyrogram.types import Message
from ..modules.vars import Config 
from .. import *
from ..modules.basic *
from ..modules.tools import get_arg

@app.on_message(commandx(["gcast"]) & SUDOERS)
async def gcast_cmd(client, message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "`Started global broadcast...`")
    else:
        return await message.edit_text("**Berikan Sebuah Pesan atau Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in BL_GCAST and chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{error}` **Grup**"
    )


@app.on_message(commandx(["gucast"]) & SUDOERS)
async def gucast(client, message: Message):
    if message.reply_to_message or get_arg(message):
        ny = await message.reply("`Started global broadcast...`")
    else:
        return await message.edit("**Berikan sebuah pesan atau balas ke pesan**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
                    await ny.delete()
    await message.edit(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
    )


@app.on_message(commandx(["addbl"]) & SUDOERS)
async def bl_chat(client, message: Message):
    if len(message.command) != 2:
        return await message.reply("**Gunakan Format:**\n `addbl [CHAT_ID]`")
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats(user_id):
        return await message.reply("Obrolan sudah masuk daftar Blacklist.")
    blacklisted = await blacklist_chat(user_id, chat_id)
    if blacklisted:
        await message.edit("Obrolan telah berhasil masuk daftar Blacklist")

@app.on_message(commandx(["delbl"]) & SUDOERS)
async def del_bl(client, message: Message):
    if len(message.command) != 2:
        return await message.reply("**Gunakan Format:**\n `delbl [CHAT_ID]`")
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats(user_id):
        return await message.reply("Obrolan berhasil dihapus dari daftar Blacklist.")
    whitelisted = await whitelist_chat(user_id, chat_id)
    if whitelisted:
        return await message.edit("Obrolan berhasil dihapus dari daftar Blacklist.")
    await message.edit("Sesuatu yang salah terjadi.")
    

@app.on_message(commandx(["blchat"]) & SUDOERS)
async def all_chats(client, message: Message):
    text = "**Daftar Blacklist Gcast:**\n\n"
    j = 0
    user_id = client.me.id
    nama_lu = await blacklisted_chats(user_id)
    for count, chat_id in enumerate(await blacklisted_chats(user_id), 1):
        try:
            title = (await client.me.id.get_chat(chat_id)).title
        except Exception:
            title = "Private\n"
        j = 1
        text += f"**{count}.{title}**`[{chat_id}]`\n"
    if j == 0:
        await message.reply("Tidak Ada Obrolan Daftar Hitam")
    else:
        await message.reply(text)
        
__NAME__ = "self"
__MENU__ = f"""
**🥀 Unduh Dan Simpan Diri\n» Foto atau Video yang Dirusak
Ke Pesan Tersimpan Anda ✨**

`.op` - Gunakan Perintah Ini Oleh\nMembalas Dengan Menghancurkan Diri Sendiri
Photo/Video.

**🌿 More Commands:**\n=> [😋🥰, wow, super, 😋😍]
"""
