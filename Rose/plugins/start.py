import asyncio
from pyrogram import *
from pyrogram import Client, filters
from ..modules.about import About
from ..modules import *
from ..modules.vars import *
from ..import *
from ..modules import mongo
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQueryResultPhoto,
    Message,
)

SUDOERS = var.SUDOERS

@bot.on_message(filters.command(["start"]) & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 Halo {message.from_user.first_name}!
	@RosePremiumBot adalah bot yang membantu mengubah akun anda jadi menjadi userbot.\n
 👉 Hubungi owner bot ini dan lakukan transaksi untuk mengaktifkan userbot kamu.\n
❓ APA PERINTAHNYA? ❓
Tekan /deploy untuk melihat semua perintah dan cara kerjanya.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
              InlineKeyboardButton(text="Feedback", callback_data="feedback"),
                ],
                [
                    InlineKeyboardButton(text="Rules", callback_data="rules"),
                    InlineKeyboardButton(text="About", callback_data="about"),
                ],
                [
              InlineKeyboardButton(text="Login", callback_data="login"),
                ],
            ]
        ),
     disable_web_page_preview=True
    )
	

@bot.on_callback_query(filters.regex("feed"))
async def feed(_, query: CallbackQuery):
      Config.feedback.append(query.from_user.id)
      button = [[InlineKeyboardButton("cancel", callback_data="cancel")]]
      markup = InlineKeyboardMarkup(button)
      await query.edit_message_text(chat_id=query.message.chat.id, text="Send your feed back here I will notify the admin.", reply_markup=markup)

@bot.on_callback_query(filters.regex("cancel"))
async def cancel(_, query: CallbackQuery):
      if query.from_user.id in Config.feedback:
         Config.feedback.remove(query.from_user.id)
      if query.from_user.id in Config.LOGIN:
         Config.LOGIN.remove(query.from_user.id)
      await start_(query, query.message)

@bot.on_callback_query(filters.regex("rules"))
async def rules(_, query: CallbackQuery):
      await query.edit_message_text(chat_id=query.message.chat.id, text=Config.RULES)

@bot.on_callback_query(filters.regex("login"))
async def login(_, query: CallbackQuery):
      Config.LOGIN.append(m.from_user.id)
      await query.edit_message_text(chat_id=query.message.chat.id, text=Config.LOGIN)
       
@bot.on_callback_query(filters.regex("reply"))
async def reply(_, query: CallbackQuery):
      id = m.data.split("+")[1]
      Config.SEND.append(id)
      await query.edit_message_text(chat_id=query.message.chat.id, text="Reply me the text which you wanted to send us")

@bot.on_callback_query(filters.regex("about"))
async def about(_, query: CallbackQuery):
      await query.edit_message_text(chat_id=query.message.chat.id, text=About.ABOUT, disable_web_page_preview=True)


@bot.on_message(filters.private & ~filters.edited)
async def incoming_private(_, message):
      user_id = message.from_user.id
      if user_id in SUDOERS:
          if not message.reply_to_message.forward_sender_name:
             return await message.reply_text("Please reply to forwarded messages only.")
                    replied_id = message.reply_to_message_id
                try:
                    replied_user_id = save[replied_id]
                except Exception as e:
                    LOGGER(e)
                    return await message.reply_text(
                        "Failed to fetch user. You might've restarted bot or some error happened. Please check logs"
                    )
                try:
                    return await bot.copy_message(
                        replied_user_id,
                        message.chat.id,
                        message.message_id,
                    )
                except Exception as e:
                    LOGGER(e)
                    return await message.reply_text(
                        "Failed to send the message, User might have blocked the bot or something wrong happened. Please check logs"
                    )
        else:
            if await mongo.is_group():
                try:
                    forwarded = await bot.forward_messages(
                        Config.LOG_GROUP_ID,
                        message.chat.id,
                        message.message_id,
                    )
                    save[forwarded.message_id] = user_id
                except:
                    pass
            else:
                for user in SUDOERS:
                    try:
                        forwarded = await bot.forward_messages(
                            user, message.chat.id, message.message_id
                        )
                        save[forwarded.message_id] = user_id
                    except:
                        pass
