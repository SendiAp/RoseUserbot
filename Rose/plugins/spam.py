import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from ..modules.vars import Config
from ..modules.basic import edit_or_reply
from ..modules.misc import extract_args
from .broadcast import BL_GCAST
from ..import *

LOG_GROUP_ID = Config.LOG_GROUP_ID

commands = ["spam", "statspam", "slowspam", "fastspam"]
SPAM_COUNT = [0]


def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 50


@app.on_message(commandx(["dspam"]) & SUDOERS)
async def delayspam(client, message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    delayspam = await extract_args(message)
    arr = delayspam.split()
    if len(arr) < 3 or not arr[0].isdigit() or not arr[1].isdigit():
        await message.edit("`Something seems missing / wrong.`")
        return
    delay = int(arr[0])
    count = int(arr[1])
    spam_message = delayspam.replace(arr[0], "", 1)
    spam_message = spam_message.replace(arr[1], "", 1).strip()
    await message.delete()

    if not spam_allowed():
        return

    for i in range(0, count):
        if i != 0:
            await asyncio.sleep(delay)
        await client.send_message(message.chat.id, spam_message)
        limit = increment_spam_count()
        if not limit:
            break

    await client.send_message(
        LOG_GROUP_ID, "**#DELAYSPAM**\nDelaySpam was executed successfully"
    )


@Client.on_message(filters.command(commands, commandx) & filters.me)
async def sspam(client: Client, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    cooldown = {"spam": 0.15, "statspam": 0.1, "slowspam": 0.9, "fastspam": 0}

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await client.send_message(message.chat.id, text)

        if message.command[0] == "statspam":
            await asyncio.sleep(0.1)
            await sent.delete()

        await asyncio.sleep(cooldown[message.command[0]])


@app.on_message(commandx(["sspam"]) & SUDOERS)
async def spam_stick(client, message):
    if not message.reply_to_message:
        await edit_or_reply(
            message, "**reply to a sticker with amount you want to spam**"
        )
        return
    if not message.reply_to_message.sticker:
        await edit_or_reply(
            message, "**reply to a sticker with amount you want to spam**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)


__NAME__ = "spam"
__MENU__ = f"""
**🥀 Spam.**

`.spam [jumlah] [teks] - **Mengirim teks secara spam dalam obrolan.**

`.delayspam [detik] [jumlah spam] [text]
Mengirim teks spam dengan jangka delay yang ditentukan!
        
© Rose Userbot
"""
