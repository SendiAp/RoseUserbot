import asyncio
import importlib

from pyrogram import idle
from uvloop import install
from . import rose as client
from .import PLUGINS, log
from .plugins import ALL_PLUGINS
from .console import LOGGER

loop = asyncio.get_event_loop()

async def rose():
    await client.start()
    log.info("Importing all plugins ...")
    for all_plugin in ALL_PLUGINS:
        imported_plugin = importlib.import_module(
            "Rose.plugins." + all_plugin)
        if (hasattr(imported_plugin, "__NAME__"
           ) and imported_plugin.__NAME__):
            imported_plugin.__NAME__ = imported_plugin.__NAME__
            if (hasattr(imported_plugin, "__MENU__"
                ) and imported_plugin.__MENU__):
                PLUGINS[imported_plugin.__NAME__.lower()
                ] = imported_plugin
        log.info(f">> Importing: {all_plugin}.py")
    log.info(">> Successfully Imported All Plugins.")
    await asyncio.sleep(1)
    log.info("Userbot is Now Ready to Use !")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(rose())
    log.info("Userbot Has Been Stopped !")
