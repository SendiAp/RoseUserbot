import asyncio

import html
from pyrogram import Client, filters, enums
from pyrogram.enums import ChatType
from pyrogram.types import *

from ..modules.basic import edit_or_reply
from ..SQL.globals import addgvar, gvarstatus
from ..modules.tools import get_arg
from .. import *
from ..modules import pmpermit as TOD
from ..modules.data import approve, disapprove, is_approved
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQueryResultPhoto,
    Message,
)

QUOTE_BUTTON = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('🔵Telegram🔵' , url='https://t.me/ItsMeSithija'),
                  InlineKeyboardButton('⭕Youtube⭕' , url='https://youtube.com/channel/UCFH_E0cu7U8GMjEJGnSvYjA'),
                ], 
                [
                 InlineKeyboardButton('〣────────────────〢' , callback_data='auto_rep'),
                ],
              ]
)


MSG_PERMIT = """
╔═════════════════════╗
   Ⓦ︎Ⓔ︎Ⓛ︎Ⓒ︎Ⓞ︎Ⓜ︎Ⓔ︎ Ⓟ︎Ⓔ︎Ⓢ︎Ⓐ︎Ⓝ︎    
╚═════════════════════╝
{}
╔═════════════════════╗
│○›ᑭᗴՏᗩᑎ OTOᗰᗩTIՏ
│○›WARNING {}/{}
│○›ᗷY ᖇOՏᗴ-ᑌՏᗴᖇᗷOT 
╚═════════════════════╝
"""

DEFAULT = """
**TOLONG JANGAN MELAKUKAN SPAM CHAT KEPADA BOS SAYA**
**KARENA SAYA AKAN OTOMATIS MEMBLOKIR KAMU, TUNGGU SAMPAI BOS SAYA MENERIMA PESAN KAMU**
"""

@app.on_message(
    (
        filters.private
        & filters.incoming
        & ~filters.service
        & ~filters.me
        & ~filters.bot
        & ~filters.via_bot
    )
)
async def pmpermit_func(client: Client, message: Message):
    user_ = message.from_user
    approved = await is_approved()
    pmper = var.PMPERMIT
    if pmper == str(False):
        return True
    if user_.is_bot:
        return
    if user_.is_self:
        return
    if user_.is_contact:
        return
    if user_.is_verified:
        return
    if user_.is_scam:
        await message.reply_text("Imposter Detected!\nAutomatic Blocking!!!")
        await client.block_user(user_.id)
        return
    if user_.is_support:
        return
    if user_.id in approved:
        return
    limits = var.PERMIT_LIMIT
    async for m in client.get_chat_history(user_.id, limit=limits):
        if m.reply_markup:
            await m.delete()
    if str(user_.id) in flood:
        flood[str(user_.id)] += 1
    else:
        flood[str(user_.id)] = 1
    if flood[str(user_.id)] > limits:
        await message.reply_text("Spammer Detected!\nAutomatic Blocking User!!!")
        if str(user_.id) in OLD_MSG:
            OLD_MSG.pop(str(user_.id))
            flood.update({user_.id: 0})
        return await client.block_user(user_.id)
    getmsg = Config.PERMIT_MSG
    pm_message = DEFAULT if not getmsg else getmsg
    pmpermit_logo = var.PMPERMIT_LOGO
    msg_dlt = await client.send_photo(
        user_.id,
        pmpermit_logo,
        MSG_PERMIT.format(pm_message, flood[str(user_.id)], limits),
    )
    if str(user_.id) in OLD_MSG:
        try:
            await OLD_MSG[str(user_.id)].delete()
        except BaseException:
            pass
    OLD_MSG[str(user_.id)] = msg_dlt


@app.on_message(commandx(["ok"]))
async def pm_approve(client: Client, message: Message):
    permit = await is_approved()
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("You can't do that to yourself.")
            return
        uid = replied_user.id
        if uid in permit:
            return await message.reply("This user already exists in the database.")
        await approve(uid)
        xnxx = await message.reply("Your message was received.")
        if str(uid) in OLD_MSG and str(uid) in flood:
            await OLD_MSG[str(uid)].delete()
            flood[str(uid)] = 0
        await asyncio.sleep(3)
        await xnxx.delete()
    else:
        aname = message.chat
        if not aname.type == ChatType.PRIVATE:
            await message.reply(
                "You're not currently in PM and you haven't replied to someone's messages."
            )
            return
        uid = aname.id
        if uid in permit:
            return await message.reply("This user already exists in the database")
        await approve(uid)
        xnxx = await message.reply("Your message was received.")
        try:
            if str(uid) in OLD_MSG and str(uid) in flood:
                await OLD_MSG[str(uid)].delete()
                flood[str(uid)] = 0
        except BaseException:
            pass
        await asyncio.sleep(3)
        await xnxx.delete()

@app.on_message(commandx("pmlimit") & SUPUSER)
async def pmguard(client: Client, message: Message):
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        return await cust_msg.edit(
            f"**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `{cmd}setvar PM_AUTO_BAN True`"
        )
    try:
        from ..SQL.globals import addgvar
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    input_str = (
        cust_msg.text.split(None, 1)[1]
        if len(
            cust_msg.command,
        )
        != 1
        else None
    )
    if not input_str:
        return await cust_msg.edit("**Harap masukan angka untuk PM_LIMIT.**")
    Ros = await cust_msg.edit("`Processing...`")
    if input_str and not input_str.isnumeric():
        return await Ros.edit("**Harap masukan angka untuk PM_LIMIT.**")
    addgvar("PM_LIMIT", input_str)
    await Ros.edit(f"**Set PM limit to** `{input_str}`")


@app.on_message(commandx("pmguard") & SUPUSER)
async def pmguard(client: Client, message: Message):
    input_str = get_arg(message)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        PMPERMIT = False
    else:
        PMPERMIT = True
    if PMPERMIT:
        if h_type:
            await edit_or_reply(message, "**PMPERMIT Sudah Diaktifkan**")
        else:
            addgvar("PMPERMIT", h_type)
            await edit_or_reply(message, "**PMPERMIT Berhasil Dimatikan**")
    elif h_type:
        addgvar("PMPERMIT", h_type)
        await edit_or_reply(message, "**PMPERMIT Berhasil Diaktifkan**")
    else:
        await edit_or_reply(message, "**PMPERMIT Sudah Dimatikan**")


@app.on_message(commandx("no") & SUPUSER)
async def pm_disapprove(client: Client, message: Message):
    permit = await is_approved()
    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.reply("You can't do that to yourself.")
            return
        uid = replied_user.id
        if uid not in permit:
            return await message.reply("User does not exist in database.")
        await disapprove(uid)
        xnxx = await message.reply("Your message has been rejected.")
        await asyncio.sleep(3)
        await xnxx.delete()
    else:
        aname = message.chat
        if aname.type != ChatType.PRIVATE:
            await message.edit(
                "You're not currently in PM and you haven't replied to someone's messages."
            )
            return
        uid = aname.id
        if uid not in permit:
            return await message.reply("User does not exist in database.")
        await disapprove(uid)
        xnxx = await message.reply("Your message has been rejected.")
        await asyncio.sleep(3)
        await xnxx.delete()


@app.on_message(commandx("block") & SUPUSER)
async def block_user_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to user message.")
    user_id = message.reply_to_message.from_user.id
    # Blocking user after editing the message so that other person can get the
    # update.
    await message.reply("Successfully Block User!!!")
    await client.block_user(user_id)


@app.on_message(commandx("unblock") & SUPUSER)
async def unblock_user_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to user message.")
    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await message.reply("Unblock User Successfully!!!")


__NAME__ = "antipm"
__MENU__ = f"""
✘ **Perintah:** `{cmds}ok`
• **Fungsi:** Terima Pesan.

✘ **Perintah:** `{cmds}no`
• **Fungsi:** Tolak Pesan.

✘ **Perintah:** `{cmds}block`
• **Fungsi:** Untuk Memblokir Pengguna.

✘ **Perintah:** `{cmds}unblock`
• **Fungsi:** Untuk Buka Blokir Pengguna.

© Rose Userbot
"""
