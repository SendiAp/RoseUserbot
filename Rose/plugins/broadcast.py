import asyncio
import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from ..modules.bc import HAPP, in_heroku
from ..modules.vars import all_vars 
from ..modules.vars import Config
from .. import *
from ..modules.basic import *
from ..modules.tools import get_arg
from ..modules import *

BLACKLIST_GCAST = Config.BLACKLIST_GCAST
BL_GCAST = [-1001599474353, -1001692751821, -1001473548283, -1001459812644, -1001433238829, -1001476936696, -1001327032795, -1001294181499, -1001419516987, -1001209432070, -1001296934585, -1001481357570, -1001459701099, -1001109837870, -1001485393652, -1001354786862, -1001109500936, -1001387666944, -1001390552926, -1001752592753, -1001777428244, -1001771438298, -1001287188817, -1001812143750, -1001883961446, -1001753840975, -1001896051491, -1001578091827, -1001704645461, -1001880331689, -1001521704453, -1001331041516, -928261650, -1001202527177, -1001810865778, -1001368023264, -1001929663249, -1001291466758, -1001617941162, -1001473548283, -1001736113681, -1001797285258, -1001797285258, -1001651242741]
BL_UBOT = [-1001812143750]
DEVS = [1307579425]

@app.on_message(commandx(["gcast","ggrups"]) & SUDOERS)
async def gcast_cmd(client, message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "`Started global broadcast...`")
    else:
        return await message.edit_text("**Berikan Sebuah Pesan atau Reply**")
    done = 0
    error = 0
    user_id = client.me.id
    list_blchat = await blacklisted_chats(user_id)
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in list_blchat and chat not in BL_GCAST:
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


@app.on_message(commandx(["gucast","gchat"]) & SUDOERS)
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

@app.on_message(commandx(["addblacklist","addbl"]) & SUDOERS)
async def addblacklist(client, message: Message):
    xxnx = await edit_or_reply(message, "`Processing...`")
    if len(message.command) != 2:
        return await message.reply("**Gunakan Format:**\n `addbl [CHAT_ID]`")
    user_id = client.me.id
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats(user_id):
        return await message.reply("Obrolan sudah masuk daftar Blacklist.")
    blacklisted = await blacklist_chat(user_id, chat_id)
    if blacklisted:
        await message.edit("Obrolan telah berhasil masuk daftar Blacklist")


@app.on_message(commandx(["delblacklist","delbl"]) & SUDOERS)
async def delblacklist(client, message: Message):
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


@app.on_message(commandx(["blchat","chat"]) & SUDOERS)
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


__NAME__ = "broadcast"
__MENU__ = f"""
**🥀 Menyiarkan pesan secara otomatis\n» ke semua obrolan groups 
dan menyiarkan pesan kesemua chat pribadi ✨**

`.gcast` [pesan] - Menyiarkan pesan kesemua groups
dalam satu waktu.

`.gucast` [pesan] - Menyiarkan pesan kesemua pengguna
chat pribadi dalam satu waktu.

`.addbl` [id] - Menambahkan daftar hitam gcast.

`.delbl` [id] - Menghapus dari daftar hitam gcast.

© Rose Userbot
"""
