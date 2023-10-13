from asyncio import create_task, sleep

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import ContentType
from aiogram.types import Message
from fluent.runtime import FluentLocalization

from ..modules.blocklists import banned, shadowbanned
from ..modules.vars import *
from ..modules import *
from ..modules.filters import SupportedMediaFilter
from ..import *


async def _send_expiring_notification(message: Message, l10n: FluentLocalization):
    """
    Mengirim pesan "penghancuran diri" setelah 5 detikMengirim pesan "penghancuran diri" setelah 5 detik

    :param message: сообщение, на которое бот отвечает подтверждением отправки
    :param l10n: объект локализации
    """
    msg = await message.reply(l10n.format_value("sent-confirmation"))
    if config.remove_sent_confirmation:
        await sleep(5.0)
        await msg.delete()


@bot.on_message(filters.command(["start"]) & filters.private)
async def cmd_start(message: Message, l10n: FluentLocalization):
    """
    Приветственное сообщение от бота пользователю

    :param message: сообщение от пользователя с командой /start
    :param l10n: объект локализации
    """
    await message.answer(l10n.format_value("intro"))


@bot.on_message(filters.command(["help"]) & filters.private)
async def cmd_help(message: Message, l10n: FluentLocalization):
    """
    Справка для пользователя

    :param message: сообщение от пользователя с командой /help
    :param l10n: объект локализации
    """
    await message.answer(l10n.format_value("help"))


@bot.message(F.text)
async def text_message(message: Message, bot: Bot, l10n: FluentLocalization):
    """
     penangan untuk pesan teks atau

    :param message: pesan dari pengguna ke admin(-ов)
    :param l10n: pesan dari pengguna ke admin lokalisasi
    """
    if len(message.text) > 4000:
        return await message.reply(l10n.format_value("too-long-text-error"))

    if message.from_user.id in banned:
        await message.answer(l10n.format_value("you-were-banned-error"))
    elif message.from_user.id in shadowbanned:
        return
    else:
        await bot.send_message(
            config.admin_chat_id,
            message.html_text + f"\n\n#id{message.from_user.id}", parse_mode="HTML"
        )
        create_task(_send_expiring_notification(message, l10n))


@bot.message(SupportedMediaFilter())
async def supported_media(message: Message, l10n: FluentLocalization):
    """
    Penangan untuk file media dari pengguna.Penangan untuk file media dari pengguna.
    Hanya tipe yang dapat ditandatangani yang didukung (lihat logger di bawah untuk daftar lengkap)

    :param message: file media dari pengguna
    :param l10n: objek lokalisasi
    """
    if message.caption and len(message.caption) > 1000:
        return await message.reply(l10n.format_value("too-long-caption-error"))
    if message.from_user.id in banned:
        await message.answer(l10n.format_value("you-were-banned-error"))
    elif message.from_user.id in shadowbanned:
        return
    else:
        await message.copy_to(
            config.admin_chat_id,
            caption=((message.caption or "") + f"\n\n#id{message.from_user.id}"),
            parse_mode="HTML"
        )
        create_task(_send_expiring_notification(message, l10n))


@bot.message()
async def unsupported_types(message: Message, l10n: FluentLocalization):
    """
    Хэндлер на неподдерживаемые типы сообщений, т.е. те, к которым нельзя добавить подпись

    :param message: сообщение от пользователя
    :param l10n: объект локализации
    """
    # Игнорируем служебные сообщения
    if message.content_type not in (
            ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER, ContentType.VIDEO_CHAT_STARTED,
            ContentType.VIDEO_CHAT_ENDED, ContentType.VIDEO_CHAT_PARTICIPANTS_INVITED,
            ContentType.MESSAGE_AUTO_DELETE_TIMER_CHANGED, ContentType.NEW_CHAT_PHOTO, ContentType.DELETE_CHAT_PHOTO,
            ContentType.SUCCESSFUL_PAYMENT, "proximity_alert_triggered",  # в 3.0.0b3 нет поддержка этого контент-тайпа
            ContentType.NEW_CHAT_TITLE, ContentType.PINNED_MESSAGE):
        await message.reply(l10n.format_value("unsupported-message-type-error"))
