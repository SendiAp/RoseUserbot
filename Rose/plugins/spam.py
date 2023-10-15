"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import asyncio
from threading import Event
from telegram.error import BadRequest
from pyrogram import Client, enums
from pyrogram.types import Message
from ..modules.basic import edit_or_reply
from ..modules.tools import extract_args
from .broadcast import BL_GCAST
from ..modules.vars import *
from ..import *

LOG_GROUP_ID = var.LOG_GROUP_ID

SPAM_COUNT = [0]
commands = ["spam", "statspam", "slowspam", "restspam"]

def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 50


@app.on_message(commandx(["dspam"]) & SUDOERS)
async def delayspam(client: Client, message: Message):
    #if message.chat.id in BL_GCAST:
    #    return await edit_or_reply(
    #        message, "**Gabisa Digunain Disini Tod!!**"
    #    )
    delayspam = await extract_args(message)
    arr = delayspam.split()
    if len(arr) < 3 or not arr[0].isdigit() or not arr[1].isdigit():
        await message.edit(f"`Format salah,\ngunakan {cmds}dspam [waktu] [jumlahspam] [kata-kata]`")
        return
    delay = int(arr[0])
    count = int(arr[1])
    spam_message = delayspam.replace(arr[0], "", 1)
    spam_message = spam_message.replace(arr[1], "", 1).strip()
    await message.delete()

    if not spam_allowed():
        return

    delaySpamEvent = Event()
    for i in range(0, count):
        if i != 0:
            delaySpamEvent.wait(delay)
        await client.send_message(message.chat.id, spam_message)
        limit = increment_spam_count()
        if not limit:
            break

    await client.send_message(
        LOG_GROUP_ID, "**#DELAYSPAM**\nDelaySpam was executed successfully"
    )


@app.on_message(filters.command(commands) & filters.me)
async def sspam(client: Client, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    cooldown = {"spam": 0, "statspam": 2.0, "slowspam": 2.5, "restspam": 1}

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
async def spam_stick(client: Client, message: Message):
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

emojis = [
    "👍",
    "👎",
    "❤️",
    "🔥",
    "🥰",
    "👏",
    "😁",
    "🤔",
    "🤯",
    "😱",
    "🤬",
    "😢",
    "🎉",
    "🤩",
    "🤮",
    "💩",
]


@app.on_message(commandx(["rspam"]) & SUDOERS)
async def reactspam(client: Client, message: Message):
    amount = int(message.command[1])
    reaction = " ".join(message.command[2:])
    await message.edit("Please wait...")
    if not message.text.split(None, 1)[1].strip():
        return await message.edit(f" gunakan: .rspam [jumlah] [emoji]")
    for i in range(amount):
        if reaction in emojis:
            try:
                await client.send_reaction(
                    message.chat.id, message.id - i, reaction
                )
            except BadRequest as e:
                if e.message.startswith("MESSAGE_ID_INVALID"):
                    # The message has been deleted or is not accessible
                    # We can't react to it, so we just continue to the next iteration
                    pass
        else:
            return await message.edit("emoji yg dipilih tidak didukung")
    await message.edit("Done!")

@app.on_message(commandx(["spam"]) & SUDOERS)
async def spam(client: Client, message: Message):
    if len(message.command) < 3:
        await edit_or_reply(
            message, "**Please use the command in the format:** `.spam (amount of sending) (message)`"
        )
        return

    try:
        times = int(message.command[1])
    except ValueError:
        await edit_or_reply(
            message, "**Please provide a valid number for the amount of sending.**"
        )
        return

    if times <= 0:
        await edit_or_reply(
            message, "**Please provide a positive number greater than zero for the amount of sending.**"
        )
        return

    spam_message = " ".join(message.command[2:])

    if not spam_message:
        await edit_or_reply(
            message, "**Please provide a message to spam with.**"
        )
        return

    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        for i in range(times):
            await client.send_message(
                message.chat.id,
                spam_message,
            )
            await asyncio.sleep(0.10)

    elif message.chat.type == enums.ChatType.PRIVATE:
        for i in range(times):
            await client.send_message(message.chat.id, spam_message)
            await asyncio.sleep(0.10)

            
__NAME__ = "spam"
__MENU__ = f"""
✘ **Perintah:** `{cmds}dspam` [waktu delay] [jumlah] [kata-kata]
• **Fungsi:** delay spam.

✘ **Perintah:** `{cmds}sspam` [balas ke stiker] [jumlah spam]
• **Fungsi:** spam stiker.

✘ **Perintah:** `{cmds}rspam` [jumlah] [emoji]
• **Fungsi:** spam reactions.

✘ **Perintah:** `{cmds}spam` [jumlah] [kata-kata]
• **Fungsi:** spam (do it with your own risk)

© Rose Userbot
"""
