"""
I am responsible for misuse of this script or code, I only correct it so that these modules and plugins function properly for other users.

https://www.github.com/SendiAp/RoseUserbot

https://t.me/RoseUserbotV2 | © Rose Userbot 
"""

import asyncio
import os

from gtts import gTTS
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from ..modules.basic import edit_or_reply

from ..import *

lang = "id"  # Default Language for voice


@app.on_message(commandx(["tts"]) & SUDOERS)
async def voice(client, message):
    global lang
    cmd = message.command
    if len(cmd) > 1:
        v_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        v_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await edit_or_reply(
            message,
            "**Balas ke pesan atau kirim argumen teks untuk mengonversi ke suara**",
        )
        return
    await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    # noinspection PyUnboundLocalVariable
    tts = gTTS(v_text, lang=lang)
    tts.save("voice.mp3")
    if message.reply_to_message:
        await asyncio.gather(
            message.delete(),
            client.send_voice(
                message.chat.id,
                voice="voice.mp3",
                reply_to_message_id=message.reply_to_message.id,
            ),
        )
    else:
        await client.send_voice(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    os.remove("voice.mp3")


@app.on_message(commandx(["voicelang"]) & SUDOERS)
async def voicelang(client, message):
    global lang
    temp = lang
    lang = message.text.split(None, 1)[1]
    try:
        gTTS("tes", lang=lang)
    except Exception:
        await edit_or_reply(message, "Wrong Language id !")
        lang = temp
        return
    await edit_or_reply(
        message, "**Bahasa untuk Voice Google diganti menjadi** `{}`".format(lang)
    )


__NAME__ = "voice"
__MENU__ = f"""
✘ **Perintah:** `{cmds}tts` [teks atau reply] 
• **Fungsi:** Ubah teks menjadi suara.

✘ **Perintah:** `{cmds}voicelang` [lang id]

**Setel bahasa suara anda
Beberapa Bahasa Suara yang Tersedia**
ID| Language  | ID| Language
af: Afrikaans | ar: Arabic
cs: Czech     | de: German
el: Greek     | en: English
es: Spanish   | fr: French
hi: Hindi     | id: Indonesian
is: Icelandic | it: Italian
ja: Japanese  | jw: Javanese
ko: Korean    | la: Latin
my: Myanmar   | ne: Nepali
nl: Dutch     | pt: Portuguese
ru: Russian   | su: Sundanese
sv: Swedish   | th: Thai
tl: Filipino  | tr: Turkish
vi: Vietname  |
zh-cn: Chinese (Mandarin/China)
zh-tw: Chinese (Mandarin/Taiwan)
            
© Rose Userbot
"""
