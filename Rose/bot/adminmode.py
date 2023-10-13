from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command
from aiogram.types import Message, Chat
from fluent.runtime import FluentLocalization

from ..modules import *

from ..modules.vars import *
bot.message.filter(F.chat.id == Config.admin_chat_id)
from .. import *

def extract_id(message: Message) -> int:
    """
    Извлекает ID юзера из хэштега в сообщении

    :param message: сообщение, из хэштега в котором нужно достать айди пользователя
    :return: ID пользователя, извлечённый из хэштега в сообщении
    """
    # Получение списка сущностей (entities) из текста или подписи к медиафайлу в отвечаемом сообщении
    entities = message.entities or message.caption_entities
    # Если всё сделано верно, то последняя (или единственная) сущность должна быть хэштегом...
    if not entities or entities[-1].type != "hashtag":
        raise ValueError("Не удалось извлечь ID для ответа!")

    # ... более того, хэштег должен иметь вид #id123456, где 123456 — ID получателя
    hashtag = entities[-1].extract_from(message.text or message.caption)
    if len(hashtag) < 4 or not hashtag[3:].isdigit():  # либо просто #id, либо #idНЕЦИФРЫ
        raise ValueError("Некорректный ID для ответа!")

    return int(hashtag[3:])


@bot.message(Command(commands=["get", "who"]), F.reply_to_message)
async def get_user_info(message: Message, bot: Bot, l10n: FluentLocalization):
    """
     Penangan untuk perintah /get dan /who. Mengambil informasi tentang pengguna.  
     Penangan untuk perintah /get dan /who. Mengambil informasi tentang pengguna.

    :param message: объект сообщения, на которое админ ответил одной из команд выше
    :param bot: объект бота, который обрабатывает текущий апдейт
    :param l10n: объект локализации
    """
    def get_full_name(chat: Chat):
        if not chat.first_name:
            return ""
        if not chat.last_name:
            return chat.first_name
        return f"{chat.first_name} {chat.last_name}"

    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    try:
        user = await bot.get_chat(user_id)
    except TelegramAPIError as ex:
        await message.reply(
            l10n.format_value(
                msg_id="cannot-get-user-info-error",
                args={"error": ex.message})
        )
        return

    u = f"@{user.username}" if user.username else l10n.format_value("no")
    await message.reply(
        l10n.format_value(
            msg_id="user-info",
            args={
                "name": get_full_name(user),
                "id": user.id,
                "username": u
            }
        )
    )


@bot.message(F.reply_to_message)
async def reply_to_user(message: Message, l10n: FluentLocalization):
    """
    Respons administrator terhadap pesan pengguna (dikirim oleh bot).    Respons administrator terhadap pesan pengguna (dikirim oleh bot).
    Metode copy_message digunakan, sehingga Anda dapat merespons dengan apa pun, bahkan polling.

    :param message: сообщение от админа, являющееся ответом на другое сообщение
    :param l10n: объект локализации
    """

    # Вырезаем ID
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    # Пробуем отправить копию сообщения.
    # В теории, это можно оформить через errors_handler, но мне так нагляднее
    try:
        await message.copy_to(user_id)
    except TelegramAPIError as ex:
        await message.reply(
            l10n.format_value(
                msg_id="cannot-answer-to-user-error",
                args={"error": ex.message})
        )
