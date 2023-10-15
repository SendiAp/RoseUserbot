import asyncio
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from ..modules.about import About
from ..modules import *
from ..modules.vars import *
from ..import *

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
              InlineKeyboardButton(text="Feedback", callback_data="feed"),
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


@bot.on_message(filters.text)
async def text(c: Client, m: Message):
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
