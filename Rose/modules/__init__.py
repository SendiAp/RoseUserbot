from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram.filters import chat
from pyrogram import Client
from typing import Dict, List, Union
from datetime import datetime, timedelta
import pymongo.errors
from platform import python_version as py
from pyrogram import __version__ as pyro
import asyncio
import codecs
import pickle
import math
import os
import dotenv
import heroku3
import requests
import urllib3
import schedule
import asyncio
from ..import *
from .vars import Config 

MONGO_DATABASE = Config.MONGO_DATABASE

mongo = MongoCli(MONGO_DATABASE)
db = mongo.app

blchatdb = db.blchat
afkdb = db.afk

async def blacklisted_chats(user_id: int) -> list:
    chats_list = []
    async for chat in blchatdb.users.find({"user_id": user_id, "chat_id": {"$lt": 0}}):
        chats_list.append(chat["chat_id"])
    return chats_list


async def blacklist_chat(user_id: int, chat_id: int) -> bool:
    if not await blchatdb.users.find_one({"user_id": user_id, "chat_id": chat_id}):
        await blchatdb.users.insert_one({"user_id": user_id, "chat_id": chat_id})
        return True
    return False


async def go_afk(user_id: int, time, reason=""):
    user_data = await afkdb.users.find_one({"user_id": user_id})
    if user_data:
        await afkdb.users.update_one({"user_id": user_id}, {"$set": {"afk": True, "time": time, "reason": reason}})
    else:
        await afkdb.users.insert_one({"user_id": user_id, "afk": True, "time": time, "reason": reason})


async def no_afk(user_id: int):
    await afkdb.users.delete_one({"user_id": user_id, "afk": True})


async def check_afk(user_id: int):
    user_data = await afkdb.users.find_one({"user_id": user_id, "afk": True})
    return user_data
      
