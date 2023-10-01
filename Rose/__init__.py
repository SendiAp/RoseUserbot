import os
from aiohttp import ClientSession
from pyrogram import Client, enums, filters
from .console import LOGGER
from .modules.core import Rose
from .modules.vars import Config
from .modules.utils import commandx
from .modules.utils import commandz

__version__ = "v2.0.1"

if Config.API_ID == 0:
    LOGGER.error("API_ID is missing! Kindly check again!")
    exit()
if not Config.API_HASH:
    LOGGER.error("API_HASH is missing! Kindly check again!")
    exit()
if not Config.BOT_TOKEN:
    LOGGER.error("BOT_TOKEN is missing! Kindly check again!")
    exit()
if not Config.STRING_SESSION:
    LOGGER.error("STRING_SESSION is missing! Kindly check again!")
    exit()
if not Config.MONGO_DATABASE:
    LOGGER.error("DATABASE_URL is missing! Kindly check again!")
    exit()
if Config.LOG_GROUP_ID == 0:
    LOGGER.error("LOG_GROUP_ID is missing! Kindly check again!")
    exit()

for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)

aiosession = ClientSession()
rose = Rose()
app = rose.app
bot = rose.bot
call = rose.call
log = LOGGER
var = Config()

db = {}

commandx = commandx
commandz = commandz

MONGO_DATABASE = Config.MONGO_DATABASE
PLUGINS = var.PLUGINS
SUPUSER = var.SUPUSER
SUDOERS = var.SUDOERS


from .modules.func import eor
eor = eor

babi = Client(
    name="babi",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Rose/modules"),
    in_memory=True,
)
