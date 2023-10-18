
from asyncio import sleep

from pyrogram import Client, enums, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from ..modules.basic import ReplyCheck

from .. import *

commands = {
    "ftyping": enums.ChatAction.TYPING,
    "fvideo": enums.ChatAction.RECORD_VIDEO,
    "faudio": enums.ChatAction.RECORD_AUDIO,
    "fround": enums.ChatAction.RECORD_VIDEO_NOTE,
    "fphoto": enums.ChatAction.UPLOAD_PHOTO,
    "fsticker": enums.ChatAction.CHOOSE_STICKER,
    "fdocument": enums.ChatAction.UPLOAD_DOCUMENT,
    "flocation": enums.ChatAction.FIND_LOCATION,
    "fgame": enums.ChatAction.PLAYING,
    "fcontact": enums.ChatAction.CHOOSE_CONTACT,
    "fstop": enums.ChatAction.CANCEL,
    "fscreen": "screenshot",
}


@app.on_message(filters.command(list(commands), cmds) & filters.me)
async def fakeactions_handler(client: Client, message: Message):
    cmd = message.command[0]
    try:
        sec = int(message.command[1])
        if sec > 60:
            sec = 60
    except:
        sec = None
    await message.delete()
    action = commands[cmd]
    try:
        if action != "screenshot":
            if sec and action != enums.ChatAction.CANCEL:
                await client.send_chat_action(chat_id=message.chat.id, action=action)
                await sleep(sec)
            else:
                return await client.send_chat_action(
                    chat_id=message.chat.id, action=action
                )
        else:
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.1)
    except Exception as e:
        return await client.send_message(
            message.chat.id,
            f"**ERROR:** `{e}`",
            reply_to_message_id=ReplyCheck(message),
        )


__NAME__ = "fakeaction"
__MENU__ = f"""
✘ **Perintah:** `{cmds}ftyping` [detik]
• **Fungsi:** Menampilkan Pengetikan Palsu dalam obrolan.

✘ **Perintah:** `{cmds}fgame` [detik] 
• **Fungsi:** Menampilkan sedang bermain game Palsu dalam obrolan.

✘ **Perintah:** `{cmds}faudio` [detik] 
• **Fungsi:** Menampilkan tindakan merekam suara palsu dalam obrolan.

✘ **Perintah:** `{cmds}fvideo` [detik] 
• **Fungsi:** Menampilkan tindakan merekam video palsu dalam obrolan.
  
✘ **Perintah:** `{cmds}fround` [detik]
• **Fungsi:** Menampilkan tindakan merekam video palsu dalam obrolan.

✘ **Perintah:** `{cmds}fphoto` [detik]
• **Fungsi:** Menampilkan tindakan mengirim foto palsu dalam obrolan.

✘ **Perintah:** `{cmds}fsticker` [detik]
• **Fungsi:** Menampilkan tindakan memilih Sticker palsu dalam obrolan.

✘ **Perintah:** `{cmds}fcontact` [detik] 
• **Fungsi:** Menampilkan tindakan Share Contact palsu dalam obrolan.

✘ **Perintah:** `{cmds}flocation` [detik] 
• **Fungsi:** Menampilkan tindakan Share Lokasi palsu dalam obrolan.

✘ **Perintah:** `{cmds}fdocument` [detik] 
• **Fungsi:** Menampilkan tindakan tengirim Document/File palsu dalam obrolan.

✘ **Perintah:** `{cmds}fscreen` [jumlah] 
• **Fungsi:** Menampilkan tindakan screenshot palsu. (Gunakan di Obrolan Pribadi)

✘ **Perintah:** `{cmds}fstop`
• **Fungsi:** Memberhentikan tindakan palsu dalam obrolan.

© Rose Userbot
"""
