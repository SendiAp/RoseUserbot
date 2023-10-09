#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import math
import os
import dotenv
import heroku3
import requests
import urllib3
import shlex
import socket
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

from .mc import restart
from .vars import *
from .vars import Config
from .vars import all_vars, all_vals
from  ..import LOGGER
from ..import *

HAPP = None

HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
LOG_GROUP_ID = Config.LOG_GROUP_ID

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def is_heroku():
    return "heroku" in socket.getfqdn()


def heroku():
    global HAPP
    if is_heroku:
        if HEROKU_API_KEY and HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(HEROKU_API_KEY)
                HAPP = Heroku.app(HEROKU_APP_NAME)
                LOGGER("Rose").info(f"Heroku App Configured")
            except BaseException as e:
                LOGGER("Heroku").error(e)
                LOGGER("Heroku").info(
                    f"Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku."
                )


async def in_heroku():
    return "heroku" in socket.getfqdn()


async def rose_log(client):
    botlog_chat_id = os.environ.get('BOTLOG_CHATID')
    if botlog_chat_id:
        return
   
    group_name = "RσʂҽUʂҽɾႦσƚ Lσɠʂ"
    group_description = 'This group is used to log my bot activities'
    group = await client.create_supergroup(group_name, group_description)

    if await is_heroku():
        try:
            Heroku = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
            happ = Heroku.client(os.environ.get('HEROKU_APP_NAME'))
            happ.Config()['LOG_GROUP_ID'] = str(group.id)
        except:
            pass
    else:
        with open('.env', 'a') as env_file:
            env_file.write(f'\nLOG_GROUP_ID={group.id}')

    message_text = 'Grouplog berhasil diaktifkan,\nmohon masukkan bot anda ke group ini, dan aktifkan mode inline.\nRestarting..!'
    await client.send_message(group.id, message_text)
    restart()
