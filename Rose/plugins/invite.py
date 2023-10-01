import asyncio

from pyrogram import Client, filters
from pyrogram.enums import ChatType, UserStatus
from pyrogram.types import Message

from ..import *
from ..modules.vars import Config
from ..modules.basic import edit_or_reply

LOG_GROUP_ID = Config.LOG_GROUP_ID

@app.on_message(commandx(["invite"]) & SUDOERS)
async def inviteee(client, message):
    mg = await edit_or_reply(message, "`Adding Users!`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")


@app.on_message(commandx(["inviteall"]) & SUDOERS)
async def inv(client, message):
    Man = await edit_or_reply(message, "`Processing . . .`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await Man.edit_text(f"inviting users from {chat.username}")
    async for member in client.get_chat_members(chat.id):
        user = member.user
        zxb = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in zxb:
            try:
                await client.add_chat_members(tgchat.id, user.id)
            except Exception as e:
                mg = await client.send_message(LOG_GROUP_ID, f"**ERROR:** `{e}`")
                await asyncio.sleep(0.3)
                await mg.delete()


@app.on_message(commandx(["invitelink"]) & SUDOERS)
async def invite_link(client, message):
    Rose = await edit_or_reply(message, "`Processing...`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await Rose.edit(f"**Link Invite:** {link}")
        except Exception:
            await Rose.edit("Denied permission")


__NAME__ = "invite"
__MENU__ = f"""
**🥀 dicoba sendiri ya ganteng atau cantik.**

`.invitelink` - **Untuk mendapatkan link invite ke grup obrolan anda. [Need Admin]**

`.invite` @username - **Untuk Mengundang Anggota ke grup Anda.**

`.inviteall` @usernamegc - **Untuk Mengundang Anggota dari obrolan grup lain ke obrolan grup anda.**

© Rose Userbot
"""
