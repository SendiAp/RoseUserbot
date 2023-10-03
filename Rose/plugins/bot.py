import random
from ..import *
from ..import bot
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from ..modules.vars import Config

OWNER_ID = Config.OWNER_ID

@bot.on_callback_query()
def pmowner(client, callback_query):
    user_id = OWNER_ID
    message = "saya ingin bertanya kak"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

roselogo = [
    "https://telegra.ph/file/d03ce0fb84f81be3aeb09.png",
]

alive_logo = random.choice(roselogo)

@bot.on_message(filters.command("/start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Yoo, saya Rose Userbot Assistant, gada yang spesial dari saya\ntapi boong..."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/RoseUserbotV2"),
            InlineKeyboardButton("Repo", url="https://github.com/SendiAp/RoseUserbot"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
