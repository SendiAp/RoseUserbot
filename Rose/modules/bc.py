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

from .vars import *
from .vars import Config
from .vars import all_vars, all_vals
from  ..import LOGGER
from ..import *

HAPP = None

BRANCH = Config.BRANCH
GIT_TOKEN = Config.GIT_TOKEN
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
REPO_URL = Config.REPO_URL
LOG_GROUP_ID = var.LOG_GROUP_ID

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(var.HEROKU_API_KEY),
    "https",
    str(var.HEROKU_APP_NAME),
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


def git():
    REPO_LINK = REPO_URL
    if GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = REPO_URL
    try:
        repo = Repo()
        LOGGER("Rose").info(f"Git Client Found")
    except GitCommandError:
        LOGGER("Rose").info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
        try:
            repo.create_remote("origin", REPO_URL)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        nrs.fetch(BRANCH)
        try:
            nrs.pull(BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install --no-cache-dir -U -r requirements.txt")
        LOGGER("Rose").info("Fetched Latest Updates")


def is_heroku():
    return "heroku" in socket.getfqdn()


def heroku():
    global HAPP
    if is_heroku:
        if var.HEROKU_API_KEY and var.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(var.HEROKU_API_KEY)
                HAPP = Heroku.app(var.HEROKU_APP_NAME)
                LOGGER("Rose").info(f"Heroku App Configured")
            except BaseException as e:
                LOGGER("Heroku").error(e)
                LOGGER("Heroku").info(
                    f"Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku."
                )


async def in_heroku():
    return "heroku" in socket.getfqdn()


async def create_botlog(client):
    if HAPP is None:
        return
    LOGGER("Rose").info(
        "TUNGGU SEBENTAR. SEDANG MEMBUAT GROUP LOG USERBOT UNTUK ANDA"
    )
    desc = "Group Log untuk Rose-UserBot.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✨ Powered By ~ Rose Userbot ✨"
    try:
        gruplog = await client.create_supergroup("Log UserBot", desc)
        if await in_heroku():
            heroku_var = HAPP.config()
            heroku_var["LOG_GROUP_ID"] = gruplog.id
        else:
            path = dotenv.find_dotenv("config.env")
            dotenv.set_key(path, "LOG_GROUP_ID", gruplog.id)
    except Exception:
        LOGGER("Rose").warning(
            "var LOG_GROUP_ID kamu belum di isi. Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id Masukan id grup nya di var LOG_GROUP_ID"
        )

async def rose_log():
    botlog_chat_id = os.environ.get('BOTLOG_CHATID')
    if botlog_chat_id:
        return
   
    group_name = "RσʂҽUʂҽɾႦσƚ Lσɠʂ"
    group_description = 'This group is used to log my bot activities'
    group = await bot1.create_supergroup(group_name, group_description)

    if await is_heroku():
        try:
            Heroku = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
            happ = Heroku.app(os.environ.get('HEROKU_APP_NAME'))
            happ.Config()['LOG_GROUP_ID'] = str(group.id)
        except:
            pass
    else:
        with open('.env', 'a') as env_file:
            env_file.write(f'\nLOG_GROUP_ID={group.id}')

    message_text = 'Grouplog berhasil diaktifkan,\nmohon masukkan bot anda ke group ini, dan aktifkan mode inline.\nRestarting..!'
    await app.send_message(group.id, message_text)
    restart()
