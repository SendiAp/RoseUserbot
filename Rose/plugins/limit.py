import asyncio
from pyrogram import Client, filters, raw
from pyrogram.types import Message
from ..import *
from ..modules.basic import edit_or_reply


@app.on_message(commandx(["limit"]) & SUDOERS)
async def spamban(client, message):
    await client.unblock_user("SpamBot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=await client.resolve_peer("SpamBot"),
            peer=await client.resolve_peer("SpamBot"),
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    Ros = await edit_or_reply(message, "`Processing...`")
    await asyncio.sleep(1)
    spambot_msg = response.updates[1].message.id + 1
    status = await app.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    await Ros.edit(f"~ {status.text}")

__NAME__ = "limit"
__MENU__ = f"""
**🌹 Command userbot:**

`.limit` - **Cek limit/batasan akun.**

© Rose Userbot
"""
