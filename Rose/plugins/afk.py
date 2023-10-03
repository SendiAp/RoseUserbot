
from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import Message
from ..modules.basic import get_text
from ..import *
from ..modules.vars import Config
from ..modules import *
from ..modules.SQL.afk_db import get_afk, set_afk

LOG_GROUP_ID = Config.LOG_GROUP_ID
DEVS = [1307579425]

@app.on_message(commandx(["afk"]) & SUDOERS)
async def afk(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        set_afk(True, message.text.split(None, 1)[1])
        await message.edit(
            "❏ {} <b>Telah AFK!</b>\n└ <b>Karena:</b> <code>{}</code>".format(
                mention_markdown(message.from_user.id, message.from_user.first_name),
                message.text.split(None, 1)[1],
            )
        )
    else:
        set_afk(True, "")
        await message.edit(
            "✘ {} <b>Telah AFK</b> ✘".format(
                mention_markdown(message.from_user.id, message.from_user.first_name)
            )
        )
    await message.stop_propagation()


@Client.on_message(
    (filters.mentioned | filters.private) & filters.incoming & ~filters.bot, group=11
)
async def afk_mentioned(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        if "-" in str(message.chat.id):
            cid = str(message.chat.id)[4:]
        else:
            cid = str(message.chat.id)

        if cid in list(AFK_RESTIRECT):
            if int(AFK_RESTIRECT[cid]) >= int(time.time()):
                return
        AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
        if get["reason"]:
            await message.reply(
                "❏ {} <b>Sedang AFK!</b>\n└ <b>Karena:</b> <code>{}</code>".format(
                    client.me.mention, get["reason"]
                )
            )
        else:
            await message.reply(
                f"<b>Maaf</b> {client.me.first_name} <b>Sedang AFK!</b>"
            )

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            if message.text:
                text = message.text
            else:
                text = message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {
                "user": message.from_user.first_name,
                "user_id": message.from_user.id,
                "chat": message.chat.title,
                "chat_id": cid,
                "text": text,
                "message_id": message.id,
            }
        )
        try:
            await client.send_message(
                LOG_GROUP_ID,
                "<b>#MENTION\n • Dari :</b> {}\n • <b>Grup :</b> <code>{}</code>\n • <b>Pesan :</b> <code>{}</code>".format(
                    message.from_user.mention,
                    message.chat.title,
                    text[:3500],
                ),
            )
        except BaseException:
            pass


@Client.on_message(filters.me & filters.group, group=12)
async def no_longer_afk(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        set_afk(False, "")
        try:
            await client.send_message(LOG_GROUP_ID, "Anda sudah tidak lagi AFK!")
        except BaseException:
            pass
        text = "<b>Total {} Mention Saat Sedang AFK<b>\n".format(len(MENTIONED))
        for x in MENTIONED:
            msg_text = x["text"]
            if len(msg_text) >= 11:
                msg_text = "{}...".format(x["text"])
            text += "- [{}](https://t.me/c/{}/{}) ({}): {}\n".format(
                escape_markdown(x["user"]),
                x["chat_id"],
                x["message_id"],
                x["chat"],
                msg_text,
            )
        try:
            await client.send_message(BOTLOG_CHATID, text)
        except BaseException:
            pass
        MENTIONED = []


__NAME__ = "afk"
__MENU__ = f"""
**🥀 kalau mau of utamakan pasang ginian biar
orang ngereply lu pada tau alasan lu gak on**

`.afk` [alasan] - **afk atau offline sementara, biar orang tau kalau lu lagi of.**

© Rose Userbot
"""
