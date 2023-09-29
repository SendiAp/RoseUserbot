from pyrogram import Client
from pyrogram import filters
from ..modules.vars import Config
import requests
from ..import *
from .import alive
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto, 
)

SUDOERS = Config.SUDOERS

@app.on_message(commandx(["alive"]))
async def alive_inline(_, inline_query):
    users = SUDOERS
    if inline_query.from_user.id not in users:
        return
     
    ALIVE_TEXT, photo_url = await alive()

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/RoseUserbotV2"),
            ],
            [
                InlineKeyboardButton("ᴅᴇᴠꜱ", url="https://t.me/pikyus1"),
                InlineKeyboardButton("ᴅᴇᴠꜱ", url="https://t.me/pikyus1"),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/smprojectID"),
            ],
        ]
    )
 
    await bot.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultPhoto(  # Use InlineQueryResultPhoto
                title="🤖 Bot Status",
                caption=ALIVE_TEXT,  # Use caption for text content
                photo_url=photo_url,
                thumb_url="https://telegra.ph/file/6cd188eddea9ae8154d1d.jpg",
                reply_markup=buttons,
            )
        ]
  )
