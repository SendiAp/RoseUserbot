"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message 
from pyrogram.errors import FloodWait
from ..import *

@app.on_message(commandx(["del"]) & SUDOERS)
async def del_msg(client, message):
    msg_src = message.reply_to_message
    if msg_src:
        if msg_src.from_user.id:
            try:
                await client.delete_messages(message.chat.id, msg_src.id)
                await message.delete()
            except BaseException:
                pass
    else:
        await message.delete()


@app.on_message(commandx(["purge"]) & SUDOERS)
async def purge(client, message):
    ex = await message.edit_text("`Starting To Purge Messages!`")
    msg = message.reply_to_message
    if msg:
        itermsg = list(range(msg.id, message.id))
    else:
        await ex.edit("`Reply To Message To Purge!`")
        return
    count = 0

    for i in itermsg:
        try:
            count = count + 1
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=i, revoke=True
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            await ex.edit(f"**ERROR:** `{e}`")
            return

    done = await ex.edit(
        f"**Fast Purge Completed!**\n**Successfully Delete** `{str(count)}` **Message.**"
    )
    await asyncio.sleep(2)
    await done.delete()

@app.on_message(commandx(["purgeme"]) & SUDOERS)
async def purgeme(client, message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await message.edit_text("Please enter a number")
    n = int(n)
    if n < 1:
        return await message.edit_text("Enter the number of messages you want to delete!")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await message.edit_text("Could not find message.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()


__NAME__ = "purgeme"
__MENU__ = f"""
✘ **Perintah:** `{cmds}del` 
• **Fungsi:** to delete someone's message.

✘ **Perintah:** `{cmds}purge`
• **Fungsi:** reply to all messages from your replied.

✘ **Perintah:** `{cmds}purgeme` [count]

© Rose Userbot
"""
