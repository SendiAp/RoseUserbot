import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message

from ..modules.vars import Config
from ..import LOGGER
from ..modules.basic import edit_or_reply
from ..modules.bc import HAPP
from ..modules.vars import all_vars, all_vals

from ..import *

LOG_GROUP_ID = Config.LOG_GROUP_ID

@app.on_message(commandx(["restart"]) & SUDOERS)
async def restart_bot(_, message: Message):
    try:
        msg = await edit_or_reply(message, "`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Rose"]
        execle(sys.executable, *args, environ)


@app.on_message(commandx(["shutdown"]) & SUDOERS)
async def shutdown_bot(client: Client, message: Message):
    if LOG_GROUP_ID:
        await client.send_message(
            LOG_GROUP_ID,
            "**#SHUTDOWN** \n"
            "**Rose-Userbot** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await edit_or_reply(message, "**Rose-Userbot Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@app.on_message(commandx(["logs"]) & SUDOERS)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    Ros = await edit_or_reply(message, "**Sedang Mengambil Logs Heroku**")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="Rose/resources/logo.jpg",
        caption="**Ini Logs Heroku anda**",
    )
    await Ros.delete()
    remove("Logs-Heroku.txt")


__NAME__ = "system"
__MENU__ = f"""
✘ **Perintah:** `{cmds}restart`
• **Fungsi:** Untuk merestart userbot.

✘ **Perintah:** `{cmds}shutdown` 
• **Fungsi:** Untuk mematikan userbot.

✘ **Perintah:** `{cmds}logs`
**Untuk melihat logs userbot.**

© Rose Userbot
"""
