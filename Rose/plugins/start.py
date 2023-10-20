from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from ..import *
from ..modules.date_info import *
from ..modules.vars import *

START_TEXT_CAPTION_TEXT = getenv("START_TEXT_CAPTION_TEXT", None)
  
INLINE_BB = InlineKeyboardMarkup(

    [

        [

            InlineKeyboardButton("Inline Mode Bot list 🔎", switch_inline_query_current_chat="")

        ]

    ]

)

REPLY_BUTTONS = [
    [
        ("Feedbacks 📝"),
        ("Rate Bots ⭐")
    ],
    [
        ("Learn Bots 👨‍🏫"),
        ("Contact 📞")

    ],
    [
        ("About Bot 🤖"),
        ("Changelog ♾️")
    ]
]

# START MESSAGE
@bot.on_message(filters.command("start") & filters.private)
async def command1(bot, message):
    text = f"Hello **{message.from_user.first_name}!**"
    reply_markup = INLINE_BB
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    await message.reply(
        "Use ReplyKeyboard or Inline Mode...",
        reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    )
    try:
        await bot.send_message(Config.LOG_GROUP_ID,
                             f"New User!\n\n◉ User - {message.from_user.first_name}\n◉ Joined time - {date_info.POSTED_TIME}\n◉ Joined date - {date_info.POSTED_DATE}")
    except Exception as er:
        print(f"Unable to send the logs to the channel.\nReason: {er}")
