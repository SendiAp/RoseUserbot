from .. import *
from .vars import *
from .. modules import *
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
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


LOG_GROUP_ID = var.LOG_GROUP_ID

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if LOG_GROUP_ID:
            Config.LOG_GROUP_ID = await bot.send_file(
                LOG_GROUP_ID,
                "https://telegra.ph/file/248b4cd5adb27bf33f15c.jpg",
                caption="**Your Wolf-Userbot has been started successfully**",
                reply_markup=QUOTE_BUTTON,
            )
