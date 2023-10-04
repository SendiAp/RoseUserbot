import asyncio
import socket
import sys
import os
import aiohttp
import asyncio
from os import getenv
from datetime import datetime
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from pyrogram import Client, filters
from pyrogram.types import Message
from ..import *
from ..modules.vars import Config, all_vars, all_vals
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
from ..import LOGGER
from ..modules.basic import edit_or_reply
HAPP = None

HEROKU_API_KEY =  Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
GIT_TOKEN = Config.GIT_TOKEN
REPO_URL = Config.REPO_URL
BRANCH = Config.BRANCH
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

BASE = "https://batbin.me/"

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def PasteBin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link

if GIT_TOKEN:
    GIT_USERNAME = REPO_URL.split("com/")[1].split("/")[0]
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
if GIT_TOKEN:
   UPSTREAM_REPO_URL = UPSTREAM_REPO
else:
   UPSTREAM_REPO_URL = REPO_URL

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])

async def is_heroku():
    return "heroku" in socket.getfqdn()

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        )
    return ch_log


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", REPO_URL)
        origin.fetch()
        repo.create_head("BRANCH", origin.refs.BRANCH)
        repo.heads.BRANCH.set_tracking_branch(origin.refs.BRANCH)
        repo.heads.BRANCH.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", REPO_URL)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@app.on_message(commandx(["update"]) & SUPUSER)
async def update_userbot(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    await message.edit("**🔄 Checking Updates ✨...**")
    update_avail = updater()
    if update_avail:
        await message.edit("**🥳 New Update Available\nFor Rose-Userbot❗**")
        asyncio.sleep(0.5)
        await message.edit("**🔃 Updating ...**")
        os.system("git pull -f && pip3 install -r Installer")
        await message.edit("**💕 Diperbarui, Sekarang Tolong\nrestart userbot anda. ✨**")
        os.system(f"kill -9 {os.getpid()} && python3 -m Rose")
        return
    else:
        await message.edit(f"**🥀 Rose Userbot Already\nUpdated To Latest 🔥 ...\n\n💕 For Any Query › Contact\nTo » @pikyus1 ✨ ...**")


@app.on_message(commandx("restart") & SUDOERS)
async def restart_bot(client, message):
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

@app.on_message(commandx("shoutdown") & SUDOERS)
async def shutdown_bot(client, message):
    if LOG_GROUP_ID:
        await client.send_message(
            LOG_GROUP_ID,
            "**#SHUTDOWN** \n"
            "**Rose-Userbot🌹** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await edit_or_reply(message, "**Rose-Premium🌹 Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


__NAME__ = "update"
__MENU__ = f"""
**🥀 Use This Plugin To Update
Your Rose Userbot.**

**🇮🇩 Command:**
`.update` - Update Your Userbot
To Latest Version.

© Rose Userbot
"""
