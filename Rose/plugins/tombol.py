from pyogram import Client
from pyrogram import filters
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


@app.on_message(commandx(["alive"]))
async def alive_inline(_, inline_query):
    user_id = (await GET_INFO.PyroX()).id
    if not inline_query.from_user.id == user_id:
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
