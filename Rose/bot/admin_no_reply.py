from aiogram import Router, F
from aiogram.types import ContentType, Message
from fluent.runtime import FluentLocalization

from ..modules import *

from ..modules.vars import *
bot.message.filter(F.chat.id == config.admin_chat_id)
from ..import *

@bot.message(~F.reply_to_message)
async def has_no_reply(message: Message, l10n: FluentLocalization):
    """
    Penangan pesan dari admin yang tidak berisi balasan (reply). Penangan pesan dari admin yang tidak berisi balasan (reply).
    Dalam hal ini, Anda perlu melakukan kesalahan.

    :param message: сообщение от админа, не являющееся ответом на другое сообщение
    :param l10n: объект локализации
    """
    if message.content_type not in (ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER):
        await message.reply(l10n.format_value("no-reply-error"))
