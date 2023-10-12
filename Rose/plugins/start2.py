
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .about import About
from ..modules.vars import *
from ..modules import *
from ..import *

START = Config.START

@bot.on_message(filters.text)
async def text(c, m):
      if m.from_user.id in Config.LOGIN:
         if m.text == Config.PASS:
            Config.LOGIN.remove(m.from_user.id)
            Config.OWNER.append(m.from_user.id)
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

@bot.on_message(filters.command(["start"]))
async def start(c, m):
      button = [[
                InlineKeyboardButton("Feedback", callback_data="feedback"),
                InlineKeyboardButton("Rules", callback_data="rules"),
                ],
                [
                InlineKeyboardButton("About", callback_data="about"),
                InlineKeyboardButton("Login", callback_data="login"),
               ]]
      markup = InlineKeyboardMarkup(button)
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START,
                           disable_web_page_preview=True,
                           reply_to_message_id=m.message_id,
                           reply_markup=markup)


@bot.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

  if "feed" in cb_data:
      Config.feedback.append(m.from_user.id)
      button = [[InlineKeyboardButton("cancel", callback_data="cancel")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="Send your feed back here I will notify the admin.", reply_markup=markup)

  if "cancel" in cb_data:
      if m.from_user.id in Config.feedback:
         Config.feedback.remove(m.from_user.id)
      if m.from_user.id in Config.LOGIN:
         Config.LOGIN.remove(m.from_user.id)
      await m.message.delete()
      await start(c, m.message)

  if "rules" in cb_data:
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=Translation.RULES)

  if "login" in cb_data:
      Config.LOGIN.append(m.from_user.id)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=Translation.LOGIN)
       
  if "yes" in cb_data:
      Config.feedback.remove(m.from_user.id)
      feedtext = m.message.reply_to_message
      button = [[InlineKeyboardButton("Reply", callback_data=f"reply+{m.from_user.id}")]]
      markup = InlineKeyboardMarkup(button)
      for i in Config.OWNER:
          NS = await feedtext.forward(int(i))
          await NS.reply_text("Send the reply", reply_markup=markup, quote=True)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="Feedback sent successfully. Hope you will get reply soon")


  if "reply" in cb_data:
      id = m.data.split("+")[1]
      Config.SEND.append(id)
      await c.send_message(chat_id=m.message.chat.id, text="Reply me the text which you wanted to send us")

  if "about" in cb_data:
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=About.ABOUT, disable_web_page_preview=True)
