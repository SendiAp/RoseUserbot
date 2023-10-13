from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup

from .pmbot.helper import captcha_buttons, captcha_text

from ..import *

from ..modules import *


@bot.on_message(filters.private & filters.command("captcha"))

def captch(bot, message):

    text = captcha_text.CAPTCHA_TEX_T

    reply_markup = InlineKeyboardMarkup(captcha_buttons.CAPTCHA_BUTT_ONS)

    bot.send_photo(message.chat.id, "https://telegra.ph/file/f54447d286c02e3f18070.jpg")

    message.reply(

        text=text,

        reply_markup=reply_markup

    )
