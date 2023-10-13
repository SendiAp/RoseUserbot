from aiogram import Router
from aiogram.types import Message
from fluent.runtime import FluentLocalization

from ..modules import *
from ..import *

@bot.edited_message()
async def edited_message_warning(message: Message, l10n: FluentLocalization):
    """
    Penangan untuk mengedit pesan.    Penangan untuk mengedit pesan.
    Saat ini, hanya ada satu reaksi terhadap pengeditan dari pihak mana pun: memberi tahu tentang ketidakmungkinan tersebut
    mengubah pesan yang diinginkan di sisi penerima.

    :param message: отредактированное пользователем или админом сообщение
    :param l10n: объект локализации
    """
    await message.reply(l10n.format_value("cannot-update-edited-error"))
