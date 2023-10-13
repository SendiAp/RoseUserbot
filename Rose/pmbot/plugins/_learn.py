
from pyrogram import Client, filters

from pyrogram import enums

from pyrogram.types import ReplyKeyboardMarkup



from ..pmbot.helper import buttons, messages

from ..import *

from ..modules import *


# Learn bots section



@bot.on_message(filters.regex(pattern="Learn Bots"))

def reply_to_Learn_Bots(bot, message):

    text = messages.LEARN_TEXT

    reply_markup = ReplyKeyboardMarkup(buttons.LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)

    message.reply(

        text=text,

        reply_markup=reply_markup,

        disable_web_page_preview=True

    )





@bot.on_message(filters.regex(pattern="Song Download Bot🤖💖"))

def reply_to_utube(bot, message):

    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)

    bot.send_message(message.chat.id,

                     "<a href=https://telegra.ph/How-to-use-Song-Downloader-Bot-07-09>How to use Song Downloader Bot?</a>")





@bot.on_message(filters.regex(pattern="Torrent Download Bot🤖💖"))

def reply_to_s_on(bot, message):

    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)

    bot.send_message(message.chat.id,

                     "<a href=https://telegra.ph/How-to-use-the-Torrent-Downloader-Bot-07-09>How to use Torrent Downloader Bot?</a>")





@bot.on_message((filters.regex(pattern="Youtube Video Download Bot🤖💖")))

def reply_to_s_ong(bot, message):

    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)

    bot.send_message(message.chat.id,

                     "<a href=https://telegra.ph/How-to-use-the-Youtube-Video-Downloader-Bot-07-09>How to use YouTube Video Download Bot?</a>")





@bot.on_message((filters.regex(pattern="Telegrph Upload Bot🤖💖")))

def reply_to_s_ong(bot, message):

    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)

    bot.send_message(message.chat.id,

                     "<a href=https://telegra.ph/How-to-use-Telegram-Telegraph-Uploader-Bot-08-09>How to use Telegraph uploader Bot?</a>")
