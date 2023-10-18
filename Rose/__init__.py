import os
import motor.motor_asyncio
from pymongo import MongoClient
from aiohttp import ClientSession
from pyrogram import Client, enums, filters
from .console import LOGGER
from .modules.core import Rose
from .modules.vars import Config
from .modules.vars import *
from .modules.utils import commandx
from .modules.utils import commandz

__version__ = "v2.0.1"

if Config.API_ID == 0:
    LOGGER.error("API_ID is missing! Kindly check again!")
    exit()
if not Config.API_HASH:
    LOGGER.error("API_HASH is missing! Kindly check again!")
    exit()
if not Config.STRING_SESSION:
    LOGGER.error("STRING_SESSION is missing! Kindly check again!")
    exit()
if not Config.MONGO_DATABASE:
    LOGGER.error("DATABASE_URL is missing! Kindly check again!")
    exit()

for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)


cmds = Config.COMMAND_PREFIXES
DB_URL = var.MONGO_DATABASE

aiosession = ClientSession()
rose = Rose()
app = rose.app
bot = rose.bot
call = rose.call
log = LOGGER
var = Config()

db = {} 
flood = {}
OLD_MSG = {}

commandx = commandx
commandz = commandz

PLUGINS = var.PLUGINS
SUPUSER = var.SUPUSER
SUDOERS = var.SUDOERS


from .modules.func import eor
eor = eor
