import asyncio
from pyrogram import *
from pyrogram import Client, filters
from ..modules.about import About
from ..modules import *
from ..modules.vars import *
from ..import *
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQueryResultPhoto,
    Message,
)

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
       
@bot.on_callback_query(filters.regex("yes"))
async def yes(_, query: CallbackQuery):
      Config.feedback.remove(query.from_user.id)
      feedtext = query.message.reply_to_message
      button = [[InlineKeyboardButton("Reply", callback_data=f"reply+{query.from_user.id}")]]
      markup = InlineKeyboardMarkup(button)
      for i in Config.OWNER_ID:
          NS = await feedtext.forward(int(i))
          await NS.reply_text("Send the reply", reply_markup=markup, quote=True)
      await query.edit_message_text(chat_id=query.message.chat.id, text="Feedback sent successfully. Hope you will get reply soon")
  
@bot.on_callback_query(filters.regex("reply"))
async def reply(_, query: CallbackQuery):
      id = m.data.split("+")[1]
      Config.SEND.append(id)
      await query.edit_message_text(chat_id=query.message.chat.id, text="Reply me the text which you wanted to send us")

@bot.on_callback_query(filters.regex("about"))
async def about(_, query: CallbackQuery):
      await query.edit_message_text(chat_id=query.message.chat.id, text=About.ABOUT, disable_web_page_preview=True)


@bot.on_message(filters.text & filters.private)
async def text(c: Client, m: Message):
      if m.from_user.id in Config.LOGIN:
         if m.text == Config.PASS:
            Config.LOGIN.remove(m.from_user.id)
            Config.OWNER_ID.append(m.from_user.id)
            await m.reply_text(text="From now you will receive feedbacks. Untill this bot restart.  If you want to get feedbacks permanently add your id in config vars")
         if m.text != Config.PASS:
            Config.LOGIN.remove(m.from_user.id)
            await m.reply_text(text="**Incorrect Password**", parse_mode="markdown")
      if m.from_user.id in Config.feedback:
         button = [[
                   InlineKeyboardButton("Yes", callback_data="yes"),
                   InlineKeyboardButton("No", callback_data="cancel")
                  ]]
         markup = InlineKeyboardMarkup(button)
         await m.reply_text(text="Are you sure to send this feedback",
                            reply_markup=markup,
                            quote=True)
      try:
          if Config.SEND is not None:
             id = Config.SEND[0]
             await c.send_message(chat_id=int(id), text=m.text, parse_mode="markdown")
             Config.SEND.remove(id)
             await c.send_message(chat_id=m.chat.id, text="Notified successfully")
      except:
          pass
