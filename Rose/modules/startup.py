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
                reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ʜᴇʟᴘ", url="t.me/BottyCu")]]
            ),
        )
    )
