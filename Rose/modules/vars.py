import os

from os import getenv
from dotenv import load_dotenv
from pyrogram import filters


if os.path.exists("Internal"):
  load_dotenv("Internal")


class Config(object):
    # REQUIRED VARIABLES
    API_ID = int(getenv("API_ID", 0))
    API_HASH = getenv("API_HASH", None)
    BOT_TOKEN = getenv("BOT_TOKEN", None)
    STRING_SESSION = getenv("STRING_SESSION", None)
    OWNER_ID= getenv("OWNER_ID", None)
    MONGO_DATABASE = getenv("MONGO_DATABASE", None)
    DATABASE_NAME = getenv("DATABASE_NAME", None)
    ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/ddd400fce0284ad813e04.jpg")
    QRIS = getenv("QRIS", "https://telegra.ph/file/29d8901cabe22ad3fd6d1.jpg")
    PMPERMIT_LOGO = getenv("PMPERMIT_LOGO", "https://telegra.ph/file/ddd400fce0284ad813e04.jpg")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    GIT_TOKEN = getenv("GIT_TOKEN", None)
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SendiAp/RoseUserbot")
    UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "rose")

  
    # OPTIONAL VARIABLES
    SESSION_STRING = getenv("SESSION_STRING", None)
    COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ".").split())
    USERBOT_PICTURE = getenv("USERBOT_PICTURE", None)
    OWNER_ID = getenv("OWNER_ID", None)
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))
    PMPERMIT = getenv("PMPERMIT", "True")
    PERMIT_MSG = getenv("PERMIT_MSG", None)
    PERMIT_LIMIT = int(getenv("PERMIT_LIMIT", 6))

    # do not edit these variables
    COMMAND_HANDLERS = {}
    PLUGINS = {}
    SUPUSER = filters.me
    SUDOERS = filters.user([])
    CRAIDUB = filters.user([])
    LRAIDUB = filters.user([])
    RRAIDUB = filters.user([])
    GBANSUB = filters.user([])
    GMUTEUB = filters.user([])
    #######################################
    for x in COMMAND_PREFIXES:
        COMMAND_HANDLERS.append(x)
    COMMAND_HANDLERS.append('')
    #######################################


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys()]
all_vals = [i for i in Config.__dict__.values()]
  
