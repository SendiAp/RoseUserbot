import os

from .. import *
from telegraph import Telegraph, upload_file
from ..modules import *
from ..modules.vars import *

telegraph = Telegraph()
filesize = 5242880 #[5MB]


@app.on_message(commandx(["tg"]) & SUDOERS)
async def telegraph_uploader(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    replied = message.reply_to_message
    m = await eor(message, "**🔄 Processing ✨...**")
    if replied:
        text_msg = replied.text
        animates = replied.animation
        media = (replied.animation or replied.photo
              or replied.video or replied.document)
        sticker =  replied.sticker
    else:
        return await m.edit(f"**🌿 Please Reply To A Media\nOr Text To Generate Telegraph\nLink❗...**")
    try:
        if text_msg:
            telegraph.create_account(short_name=f"{message.from_user.first_name}")
            author_name = str(message.from_user.first_name)
            author_url = f"https://t.me/{message.from_user.username}" if message.from_user.username else "https://t.me/AdityaServer"
            if len(message.command) > 1:
                text_title = ' '.join(message.command[1:])
            else:
                text_title = str(message.from_user.first_name + " " + (message.from_user.last_name or ""))
            await m.edit("**📤 Uploading ✨...**")
            response = telegraph.create_page(title=text_title, html_content=text_msg, author_name=author_name, author_url=author_url)
            upload_link = f"https://telegra.ph/{response['path']}"
            return await m.edit(
                text=f"**✅ Uploaded To Telegraph.**\n\n `{upload_link}`",
                disable_web_page_preview=True,
            )
        elif media:
            if media.file_size <= filesize:
                await m.edit("**📥 Downloading ✨...**")
                local_path = f"./downloads/{user_id}_{media.file_unique_id}/"
                local_file = await replied.download(local_path)
            else:
                return await m.edit("`🌺 File Size is Too Big❗...`")
        elif sticker:
            return await m.edit("`🚫 Sorry, Sticker Upload\nNot Allowed❗...`")
        else:
            return
        await m.edit("**📤 Uploading ✨...**")
        upload_path = upload_file(local_file)
        upload_link = f"https://telegra.ph{upload_path[0]}"
        await m.edit(
            text=f"**✅ Uploaded To Telegraph.**\n\n `{upload_link}`",
            disable_web_page_preview=True,
        )
        os.system(f"rm -rf {local_path}")
    except Exception as e:
        await m.edit(f"**🚫 Error:** `{e}`")
        pass


__NAME__ = "telegraph"
__MENU__ = """
✘ **Perintah:** `{cmds}tg` 
• **Fungsi:** Balas perintah ini Ke balas perintah Ini ke teks atau media apa pun untuk dibuat
tautan telegraf.

✘ **Perintah:** `{cmds}tg` [title] 
• **Fungsi:** Tetapkan judul kustom di pos telegraf anda
(Hanya Bekerja Pada Posting Teks).

© Rose Userbot 
"""
