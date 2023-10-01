import asyncio
import importlib

from pyrogram import idle
from uvloop import install
from . import babi
from . import rose as client
from .import PLUGINS, log
from .plugins import ALL_PLUGINS
from .console import LOGGER
from . import LOG_GROUP_ID, COMMAND_PREFIXES

loop = asyncio.get_event_loop()

import importlib

BOT_VER = "1.0"

MSG_ON = """
🔥 **PyroMan-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_plugin in ALL_PLUGINS:
        importlib.import_module(f"Rose.modules.{all_module}")
    for bot in babi:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Lunatic0de")
            await bot.join_chat("SharingUserbot")
            try:
                await bot.send_message(
                    LOG_GROUP_ID, MSG_ON.format(BOT_VER, COMMAND_PREFIXES)
                )
            except BaseException:
                pass
            LOGGER("ProjectMan").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("rose").warning(a)
    LOGGER("ProjectMan").info(f"PyroMan-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectMan").info("Starting PyroMan-UserBot")
    install()
    LOOP.run_until_complete(main())
