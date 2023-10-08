
import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from ..import *
from ..modules import *
from ..modules.tools import get_arg
from ..modules.vars import *


@app.on_message(filters.group & filters.mentioned & filters.incoming & ~filters.bot & ~filters.via_bot)
async def log_tagged_messages(client, message):
    chat_id = message.chat.id
    user_id = client.me.id
    botlog_chat_id = var.LOG_GROUP_ID
    knl = f"📨<b><u>ANDA TELAH DI TAG</u></b>\n<b> • Dari : </b>{message.from_user.mention}"
    knl += f"\n<b> • Grup : </b>{message.chat.title}"
    knl += f"\n<b> • 👀 </b><a href = '{message.link}'>Lihat Pesan</a>"
    knl += f"\n<b> • Message : </b><code>{message.text}</code>"
    await asyncio.sleep(0.5)
    await client.send_message(
        botlog_chat_id,
        knl,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )
