from aiogram import Router, F
from aiogram.types import Message
from fluent.runtime import FluentLocalization

from ..modules.vars import *
from ..import *


@bot.message(F.reply_to_message, F.chat.id == config.admin_chat_id, F.poll)
async def unsupported_admin_reply_types(message: Message, l10n: FluentLocalization):
    """
    Penangan untuk jenis pesan yang tidak didukung, mis. yang tidak masuk akal    Penangan untuk jenis pesan yang tidak didukung, mis. yang tidak masuk akal
    untuk menyalin. Misalnya polling (admin tidak akan melihat hasilnya)

    :param message: сообщение от администратора
    :param l10n: объект локализации
    """
    await message.reply(l10n.format_value("cannot-reply-with-this-type-error"))
