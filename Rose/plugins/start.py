import html
from ..modules import *
from ..modules.vars import *
from .. import *
from pyrogram import Client, filters, idle, enums
from pyrogram.types import Message, User
from ..modules.humanbytes import humanbytes

IF_TEXT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
IF_CONTENT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

owner_id = var.OWNER_ID

@bot.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == owner_id:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=owner_id,
        text=IF_TEXT.format(reference_id, info.first_name, message.text),
        parse_mode=enums.ParseMode.HTML,
    )

@bot.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == owner_id:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=owner_id,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=IF_CONTENT.format(reference_id, info.first_name),
        parse_mode=enums.ParseMode.HTML,
    )

@bot.on_message(filters.user(owner_id) & filters.text & filters.private)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )  
       
@bot.on_message(filters.user(owner_id) & filters.media & filters.private)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode=enums.ParseMode.HTML,
        )   
