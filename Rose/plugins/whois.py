from asyncio import gather
from os import remove

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from ..modules.basic import edit_or_reply
from ..modules.basic import ReplyCheck
from ..modules.tools import extract_user

from ..import *


@app.on_message(commandx(["info"]) & SUDOERS)
async def chatinfo_handler(client, message):
    Ros = await edit_or_reply(message, "`Processing...`")
    try:
        if len(message.command) > 1:
            chat_u = message.command[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await message.edit(
                    f"Gunakan perintah ini di dalam grup atau gunakan `{cmd}chatinfo [group username atau id]`"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""<b>CHAT INFORMATION:</b>

🆔 <b>Chat ID:</b> <code>{chat.id}</code>
👥 <b>Title:</b> {chat.title}
👥 <b>Username:</b> {username}
📩 <b>Type:</b> <code>{type}</code>
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🗣️ <b>Is Scam:</b> <code>{chat.is_scam}</code>
🎭 <b>Is Fake:</b> <code>{chat.is_fake}</code>
✅ <b>Verified:</b> <code>{chat.is_verified}</code>
🚫 <b>Restricted:</b> <code>{chat.is_restricted}</code>
🔰 <b>Protected:</b> <code>{chat.has_protected_content}</code>

🚻 <b>Total members:</b> <code>{chat.members_count}</code>
📝 <b>Description:</b>
<code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Ros.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await Ros.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Ros.edit(f"**INFO:** `{e}`")


__NAME__ = "info"
__MENU__ = f"""
**🥀 Command Info:.**

`.whois` - **dapatkan info pengguna telegram dengan deskripsi lengkap.**

`.info` - **dapatkan info group dengan deskripsi lengkap.**

© Rose Userbot
"""
