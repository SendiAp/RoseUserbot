
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from .broadcast import BL_GCAST
from ..modules.basic import edit_or_reply

from ..import *


@app.on_message(commandx(["join"]) & SUDOERS)
async def join(client, message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**Berhasil Bergabung ke Chat ID** `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@app.on_message(commandx(["kickme", "leave"]) & SUDOERS)
async def leave(client, message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    if message.chat.id in BL_GCAST:
        return await xxnx.edit("**Perintah ini Dilarang digunakan di Group ini**")
    try:
        await xxnx.edit_text(f"{client.me.first_name} has left this group, bye!!")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@app.on_message(commandx(["leaveallgc"]) & SUDOERS)
async def kickmeall(client, message):
    Man = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )


@app.on_message(commandx(["leaveallch"]) & SUDOERS)
async def kickmeallch(client, message):
    Man = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"**Berhasil Keluar dari {done} Channel, Gagal Keluar dari {er} Channel**"
    )


__NAME__ = "joinleave"
__MENU__ = f"""
**🥀 Join leave naik gc atau channel atau keluar 
otomatis menggunakan bot✨**

`.kickme` - Keluar dari grup dengan menampilkan pesan has left this group, bye!!.

`.join` [username] - Untuk Bergabung dengan Obrolan Melalui username.

`.leave` [username] - Untuk keluar dari grup Melalui username.

`.leaveallch` - Keluar dari semua channel telegram yang anda gabung.

`.leaveallgc` - Keluar dari semua grup telegram yang anda gabung.

© Rose Userbot
"""
  
