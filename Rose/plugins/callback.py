import pyrogram
from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..modules.vars import *
from ..modules import *
from ..import *
from ..modules.about import About
from .start import *

@app.on_callback_query(filters.regex("feed"))
async def feed(_, query: CallbackQuery):
      Config.feedback.append(query.from_user.id)
      button = [[InlineKeyboardButton("cancel", callback_data="cancel")]]
      markup = InlineKeyboardMarkup(button)
      await query.delete()
      await query.send_message(chat_id=m.message.chat.id, text="Send your feed back here I will notify the admin.", reply_markup=markup)

@app.on_callback_query(filters.regex("cancel"))
async def cancel(_, query: CallbackQuery):
      if query.from_user.id in Config.feedback:
         Config.feedback.remove(m.from_user.id)
      if query.from_user.id in Config.LOGIN:
         Config.LOGIN.remove(m.from_user.id)
      await query.delete()
      await start(query, query.message)

@app.on_callback_query(filters.regex("rules"))
async def rules(_, query: CallbackQuery):
      await query.delete()
      await query.send_message(chat_id=m.message.chat.id, text=Config.RULES)

@app.on_callback_query(filters.regex("login"))
async def login(_, query: CallbackQuery):
      Config.LOGIN.append(m.from_user.id)
      await query.delete()
      await query.send_message(chat_id=m.message.chat.id, text=Config.LOGIN)
       
@app.on_callback_query(filters.regex("yes"))
async def yes(_, query: CallbackQuery):
      Config.feedback.remove(m.from_user.id)
      feedtext = query.message.reply_to_message
      button = [[InlineKeyboardButton("Reply", callback_data=f"reply+{query.from_user.id}")]]
      markup = InlineKeyboardMarkup(button)
      for i in Config.OWNER:
          NS = await feedtext.forward(int(i))
          await NS.reply_text("Send the reply", reply_markup=markup, quote=True)
      await query.delete()
      await query.send_message(chat_id=m.message.chat.id, text="Feedback sent successfully. Hope you will get reply soon")
  
@app.on_callback_query(filters.regex("reply"))
async def reply(_, query: CallbackQuery):
      id = m.data.split("+")[1]
      Config.SEND.append(id)
      await query.send_message(chat_id=m.message.chat.id, text="Reply me the text which you wanted to send us")

@app.on_callback_query(filters.regex("about"))
async def about(_, query: CallbackQuery):
      await query.delete()
      await query.send_message(chat_id=m.message.chat.id, text=About.ABOUT, disable_web_page_preview=True)
