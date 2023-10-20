#rose Userbot 2023

import requests

from .. import *


@app.on_message(commandx(["pen", "write"]) & SUDOERS)
async def handwrite(client, message):
    replied = message.reply_to_message
    msg = f"**Please Reply To A Text Or Give Some Lines To Write !**"
    if replied:
        if replied.text or replied.caption:
            text = replied.text or replied.caption
        else:
            return await message.reply_text(msg)
    else:
        if len(message.command) > 1:
            text = message.text.split(None, 1)[1]
        else:
            return await eor(message, msg)
    m = await eor(message, "**Please Wait ...**")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url
    caption = f"**Successfully Written Your Text.**"
    try:
        if message.from_user.id != app.id:
            await message.reply_photo(photo=write, caption=caption)
            await m.delete()
        else:
            await app.send_photo(message.chat.id, photo=write, caption=caption)
            await m.delete()
    except Exception as e:
        await m.edit(f"**Error:** `{e}`")
        
    
 
 
__NAME__ = "write"
__MENU__ = f"""
✘ **Perintah:** `{cmds}write` [text]
• **Fungsi:** Untuk Menulis TeksUntuk Menulis Teks
Di Halaman Putih.

© Rose Userbot 
"""
