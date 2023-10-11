"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""



import asyncio

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from ..import *
from ..modules.basic import edit_or_reply
from ..modules.mc import extract_user, extract_user_and_reason, list_admins

DEVS = [1307579425]

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@app.on_message(commandx(["setchatphoto", "setgpic"]) & SUDOERS)
async def set_chat_photo(client, message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("You don't have enough permission")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("Reply to a photo to set it !")


@app.on_message(commandx(["ban", "cban"]) & SUDOERS)
async def member_ban(client, message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't ban myself.")
    if user_id in DEVS:
        return await Man.edit("I can't ban my developer!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't ban an admin, You know the rules, so do i.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**Banned User:** {mention}\n"
        f"**Banned By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.ban_member(user_id)
    await Man.edit(msg)


@app.on_message(commandx(["unban", "cunban"]) & SUDOERS)
async def member_unban(client, message):
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await Man.edit("You cannot unban a channel")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await Man.edit(
            "Provide a username or reply to a user's message to unban."
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await Man.edit(f"Unbanned! {umention}")


@app.on_message(commandx(["pin", "unpin"]) & SUDOERS)
async def pin_message(client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Reply to a message to pin/unpin it.")
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await Man.edit("I don't have enough permissions")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await Man.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await Man.edit(
        f"**Pinned [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )


@app.on_message(commandx(["mute", "cmute"]) & SUDOERS)
async def mute(client, message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't mute myself.")
    if user_id in DEVS:
        return await Man.edit("I can't mute my developer!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't mute an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await Man.edit(msg)


@app.on_message(commandx(["unmute", "cunmute"]) & SUDOERS)
async def unmute(client, message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Unmuted! {umention}")


@app.on_message(commandx(["kick", "dkick"]) & SUDOERS)
async def kick_user(client, message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't kick myself.")
    if user_id == DEVS:
        return await Man.edit("I can't kick my developer.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't kick an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await Man.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await Man.edit("**Maaf Anda Bukan admin**")


@app.on_message(commandx(["promote", "fullpromote"]) & SUDOERS)
async def promotte(client, message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    Man = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await Man.edit("I can't find that user.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await Man.edit("I don't have enough permissions")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await Man.edit(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await Man.edit(f"Promoted! {umention}")


@app.on_message(commandx(["demote", "cdemote"]) & SUDOERS)
async def demote(client, message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't demote myself.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Demoted! {umention}")

__NAME__ = "admin"
__MENU__ = f"""
✘ **Perintah:** `.ban` [reply username/userid] [alasan]
• **Fungsi:** Membanned pengguna dari groups.

✘ **Perintah:** `.unban` [reply username/userid]
• **Fungsi:** Menghapus pengguna dari banned groups.

✘ **Perintah:** `.kick` [reply username/userid] 
• **Fungsi:** Keluarkan pengguna dari groups.

✘ **Perintah:** `.promote` [reply user]
• **Fungsi:** Mempromosikan pengguna menjadi admin groups.

✘ **Perintah:** `.delmote` [reply user]
• **Fungsi:** Menghapus pengguna dari admin groups.

✘ **Perintah:** `.mute` [reply] 
• **Fungsi:** Membisukan pengguna dari groups.

✘ **Perintah:** `.unmute` [reply]
• **Fungsi:** Menghapus bisu pengguna dari groups.

✘ **Perintah:** `.pin` [reply] 
• **Fungsi:** Menyematkan pesan / gambar dll digroups.

✘ **Perintah:** `.unpin` [reply] 
• **Fungsi:** Melepas semat postingan groups.

✘ **Perintah:** `.setgpic [reply foto] 
• **Fungsi:** Memasang foto groups.

© Rose Userbot
"""
