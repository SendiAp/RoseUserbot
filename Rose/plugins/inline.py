import asyncio

from pyrogram.types import Message
from pyrogram import Client
from .. import *
from .. import __version__
from ..modules.misc import *
from ..modules.utils import *
from pyrogram.types import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQueryResultPhoto,
    Message,
)

num_basic_modules = len(PLUGINS)

async def help_menu_logo(answer):
    if var.USERBOT_PICTURE:
        thumb_image = var.USERBOT_PICTURE
    else:
        thumb_image = "https://telegra.ph/file/027283ee9defebc3298b8.png"
    button = paginate_plugins(0, PLUGINS, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="🥀 Help Menu ✨",
            thumb_url=f"{thumb_image}",
            description=f"🥀 Open Help Menu Of Rose-Userbot ✨...",
            caption=f"""
尺ㄖ丂乇 ㄩ丂乇尺乃ㄖㄒ

᳇ Help Menu: {message.from_user.first_name} 
• Version: {__version__} 
• Modules: {num_basic_modules}"""
            """,
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    button = paginate_plugins(0, PLUGINS, "help")
    answer.append(
        InlineQueryResultArticle(
            title="🥀 Help Menu ✨",
            input_message_content=InputTextMessageContent(f"""
尺ㄖ丂乇 ㄩ丂乇尺乃ㄖㄒ

᳇ Help menu: {message.from_user.first_name} 
• version: {__version__} 
• modules: {num_basic_modules}""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


@bot.on_inline_query()
@inline_wrapper
async def inline_query_handler(bot, query):
    text = query.query
    if text.startswith("help_menu_logo"):
        answer = []
        answer = await help_menu_logo(answer)
        try:
            await bot.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except Exception as e:
            print(str(e))
            return
    elif text.startswith("help_menu_text"):
        answer = []
        answer = await help_menu_text(answer)
        try:
            await bot.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except Exception as e:
            print(str(e))
            return
    else:
        return
