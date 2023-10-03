
from gpytranslate import Translator
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from ..modules.basic import edit_or_reply

from ..import *


@app.on_message(commandx(["tr"]) & SUDOERS)
async def translate(client, message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        input_str = (
            message.text.split(None, 1)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        target = input_str or "id"
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await edit_or_reply(
                message,
                f"**ERROR:** `{str(err)}`",
                parse_mode=enums.ParseMode.MARKDOWN,
            )
            return
    else:
        input_str = (
            message.text.split(None, 2)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        text = message.text.split(None, 2)[2]
        target = input_str or "id"
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await edit_or_reply(
                message,
                "**ERROR:** `{}`".format(str(err)),
                parse_mode=enums.ParseMode.MARKDOWN,
            )
            return
    await edit_or_reply(
        message,
        f"**Diterjemahkan ke:** `{target}`\n```{tekstr.text}```\n\n**Bahasa yang Terdeteksi:** `{(await trl.detect(text))}`",
        parse_mode=enums.ParseMode.MARKDOWN,
    )


__NAME__ = "translate"
__MENU__ = f"""
**🥀 Menerjemahkan bahasa asing.**

`.tr` [kode bahasa] - **Menerjemahkan teks ke bahasa yang disetel. .**

(Default kode bahasa indonesia)

© Rose Userbot
"""
