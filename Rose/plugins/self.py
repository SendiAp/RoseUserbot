import os

from .. import *
from pyrogram import filters


@app.on_message(commandz(["😋🥰", "op", "wow", "super", "😋😍"])
    & filters.private & filters.me)
async def self_media(client, message):
    replied = message.reply_to_message
    if not replied:
        return
    if not (replied.photo or replied.video):
        return
    location = await client.download_media(replied)
    await client.send_document("me", location)
    os.remove(location)


__NAME__ = "self"
__MENU__ = f"""
**🥀 Unduh Dan Simpan Diri\n» Foto atau Video yang Dirusak
Ke Pesan Tersimpan Anda ✨**

`.op` - Gunakan Perintah Ini Oleh\nMembalas Dengan Menghancurkan Diri Sendiri
Photo/Video.

**🌿 More Commands:**\n=> [😋🥰, wow, super, 😋😍]
"""
