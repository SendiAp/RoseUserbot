from pyrogram import Client, filters
from pyrogram.types import Message

from ..import **
from ..modules.basic import edit_or_reply


@app.on_message(commandx(["create", "buat"]) & SUDOERS)
async def create(client, message):
    if len(message.command) < 3:
        return await edit_or_reply(
            message, f"**Ketik {cmd}help create bila membutuhkan bantuan**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    Man = await edit_or_reply(message, "`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Berhasil Membuat Group Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Berhasil Membuat Channel Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


__NAME__ = "create"
__MENU__ = f"""
**🥀 Buat yang males buka tombol apapun
buat gc atau ch pake perintah ini aja.**

`.create ch` - **Untuk membuat channel telegram dengan userbot.**
`.create gc` - **Untuk membuat group telegram dengan userbot.**

© Rose Userbot
"""
