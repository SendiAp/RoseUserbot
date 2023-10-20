# Rose Userbot| Rose

from .. import *
from ..modules.func import *
from ..modules.utils import *

from pyrogram import *
from pytgcalls import StreamType
from pytgcalls.types.input_stream import *
from pytgcalls.types.input_stream.quality import *


# Audio Stream
@app.on_message(commandx(["play", "rplay"]) & SUDOERS)
async def audio_stream(client, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    audio = (
        (replied.audio or replied.voice or
        replied.video or replied.document)
        if replied else None
    )
    m = await eor(message, "**🔄 Processing ...**")
    try:
        if audio:
            await m.edit("**📥 Downloading ...**")
            file = await replied.download()
        else:
            if len(message.command) < 2:
                 return await m.edit("**🤖 Give Some Query ...**")
            text = message.text.split(None, 1)[1]
            if "?si=" in text:
                query = text.split("?si")[0]
            else:
                query = text
            await m.edit("**🔍 Searching ...**")
            search = get_youtube_video(query)
            stream = search[0]
            file = await get_youtube_stream(stream)
        await m.edit("**🔄 Processing ...**")
        check = db.get(chat_id)
        if not check:
            await call.join_group_call(
                chat_id,
                AudioPiped(
                    file,
                    HighQualityAudio(),
                ),
                stream_type=StreamType().pulse_stream
            )
            await put_que(chat_id, file, "Audio")
            await m.edit("**🥳 Berhasil memulai streaming audio!**\n\n**Powered By: Rose Userbot**")
        else:
            pos = await put_que(chat_id, file, "Audio")
            await m.edit(f"**😋 Audio berikutnya ditambahkan ke posisi #{pos}**\n\n**Powered By: Rose Userbot**")
    except Exception as e:
        await m.edit(f"**Error:** `{e}`")

  
# Video Stream
@app.on_message(commandx(["vplay", "rvplay"]) & SUDOERS)
async def video_stream(client, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    video = (
        (replied.audio or replied.voice or
        replied.video or replied.document)
        if replied else None
    )
    m = await eor(message, "**🔄 Processing ...**")
    try:
        if video:
            await m.edit("**📥 Downloading ...**")
            file = await replied.download()
        else:
            if len(message.command) < 2:
                 return await m.edit("**🤖 Give Some Query ...**")
            text = message.text.split(None, 1)[1]
            if "?si=" in text:
                query = text.split("?si")[0]
            else:
                query = text
            await m.edit("**🔍 Searching ...**")
            search = get_youtube_video(query)
            stream = search[0]
            file = await get_youtube_stream(stream)
        await m.edit("**🔄 Processing ...**")
        check = db.get(chat_id)
        if not check:
            await call.join_group_call(
                chat_id,
                AudioVideoPiped(
                    file,
                    HighQualityAudio(),
                    HighQualityVideo(),
                ),
                stream_type=StreamType().pulse_stream
            )
            await put_que(chat_id, file, "Video")
            await m.edit("🥳 **Berhasil memulai streaming video!**\n\n**Powered By: Rose Userbot**")
        else:
            pos = await put_que(chat_id, file, "Video")
            await m.edit(f"**😋 Video berikutnya ditambahkan ke posisi #{pos}**\n\n**Powered By: Rose Userbot**")
    except Exception as e:
        await m.edit(f"**Error:** `{e}`")


# Pause Stream
@app.on_message(commandx(["pause", "pse"]) & SUDOERS)
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            await call.pause_stream(chat_id)
            return await eor(message, "**Stream Paused !**")
        else:
            return await eor(message, "**Nothing Playing !**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")


# Resume Stream
@app.on_message(commandx(["resume", "rsm"]) & SUDOERS)
async def resume_streams(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            await call.resume_stream(chat_id)
            return await eor(message, "**Stream Resumed !**")
        else:
            return await eor(message, "**Nothing Playing !**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")
        
        
# Skip To Next Stream
@app.on_message(commandx(["skip", "skp"]) & SUDOERS)
async def change_streams(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            que = db[chat_id]
            que.pop(0)
            if len(que) == 0:
                await call.leave_group_call(chat_id)
                return await eor(message, "Empty Queue !")
            else:
                file = check[0]["file"]
                type = check[0]["type"]
                if type == "Audio":
                    stream = AudioPiped(
                        file,
                        HighQualityAudio(),
                    )
                elif type == "Video":
                    stream = AudioVideoPiped(
                        file,
                        HighQualityAudio(),
                        HighQualityVideo(),
                    )
                await call.change_stream(chat_id, stream)
                return await eor(message, "🥳 Skipped !")
        else:
            return await eor(message, "**Nothing Playing ...**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")


# Stop/End Stream
@app.on_message(commandx(["end", "stop"]) & SUDOERS)
async def leave_streams(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            check.pop(0)
            await call.leave_group_call(chat_id)
            return await eor(message, "**Stream Stopped !**")
        else:
            return await eor(message, "**Nothing Playing !**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")


__NAME__ = "vcbot"
__MENU__ = f"""
✘ **Perintah:** `{cmds}play` [name] 
• **Fungsi:** Putar audio lagu Dengan memberi nama.

✘ **Perintah:** `{cmds}vplay` [name]
• **Fungsi:** Putar video lagu dengan memberi nama.

✘ **Perintah:** `{cmds}pause` - To pause stream.
✘ **Perintah:** `{cmds}resume` - To resume stream.
✘ **Perintah:** `{cmds}skip` - Skip to Next song.
✘ **Perintah:** `{cmds}end` - To stop stream.

© Rose Userbot
"""
