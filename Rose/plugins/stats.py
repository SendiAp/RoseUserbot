"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

from datetime import datetime

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from ..modules.basic import edit_or_reply

from ..import *


@app.on_message(commandx(["stats"]) & SUDOERS)
async def stats(client, message):
    Ros = await edit_or_reply(message, "`Collecting stats...`")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await Ros.edit_text(
        """`Your Stats Obtained in {} seconds`
`You have {} Private Messages.`
`You are in {} Groups.`
`You are in {} Super Groups.`
`You Are in {} Channels.`
`You Are Admin in {} Chats.`
`Bots = {}`""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )


__NAME__ = "stats"
__MENU__ = f"""
✘ **Perintah:** `{cmds}stats` 
• **Fungsi:** To Check Your Account Status, how Joined Chats.

© Rose Userbot
"""
