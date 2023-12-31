from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from ..modules.basic import edit_or_reply
from ..modules.tools import get_arg

from ..import *


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"**No group call Found** {err_msg}")
    return False


@app.on_message(commandx(["startvc"]) & SUDOERS)
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    Ros = await edit_or_reply(message, "`Processing . . .`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"**Started Group Call\n • **Chat ID** : `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • **Title:** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await Ros.edit(args)
    except Exception as e:
        await Ros.edit(f"**INFO:** `{e}`")


@app.on_message(commandx(["stopvc"]) & SUDOERS)
async def end_vc_(client, message):
    """End group call"""
    chat_id = message.chat.id
    if not (
        group_call := (
            await get_group_call(client, message, err_msg=", group call already ended")
        )
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await edit_or_reply(message, f"Ended group call in **Chat ID** : `{chat_id}`")


@app.on_message(commandx(["joinvc"]) & SUDOERS)
async def joinvc(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        Ros = await message.reply("`Otw Naik...`")
    else:
        Ros = await message.edit("`Otw Naik....`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
    except Exception as e:
        return await Ros.edit(f"**ERROR:** `{e}`")
    await Ros.edit(f"**Berhasil Join Ke Obrolan Group**\n└ **Chat ID:** `{chat_id}`")
    await asyncio.sleep(200)
    await Ros.delete()

@app.on_message(commandx(["leavevc"]) & SUDOERS)
async def leavevc(client: Client, message: Message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        Ros = await message.reply("`Turun Dulu...`")
    else:
        Ros = await message.edit("`Turun Dulu....`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await call.leave_group_call(chat_id)
    except Exception as e:
        return await edit_or_reply(message, f"**ERROR:** `{e}`")
    msg = "**Berhasil Turun dari Obrolan Suara**"
    if chat_id:
        msg += f"\n└ **Chat ID:** `{chat_id}`"
    await Ros.edit(msg)
    await asyncio.sleep(3)
    await Ros.delete(msg)



__NAME__ = "vcg"
__MENU__ = f"""
✘ **Perintah:** `{cmds}startvc` 
• **Fungsi:** Untuk Memulai voice chat group.

✘ **Perintah:** `{cmds}stopvc` 
• **Fungsi:** Untuk Memberhentikan voice chat group.

✘ **Perintah:** `{cmds}joinvc` 
• **Fungsi:** Untuk Bergabung ke voice chat group.

✘ **Fungsi:** `{cmds}leavevc` 
• **Fungsi:** Untuk Turun dari voice chat group.

© Rose Userbot
"""
