# Rose Userbot 2023

import asyncio

from .. import *
from ..modules.vars import all_vars
from ..modules.vars import all_vals


@app.on_message(commandx("vars") & SUPUSER)
async def all_vars_(client, message):
    await message.edit("**Please Wait ...**")
    await asyncio.sleep(1)
    await message.edit(f"{all_vars}")
    
@app.on_message(commandx("vals") & SUPUSER)
async def all_vals_(client, message):
    await message.edit("**Please Wait ...**")
    await asyncio.sleep(1)
    await message.edit(f"{all_vals}")



__NAME__ = "vars"
__MENU__ = """**Dapatkan Variabel Userbot Anda
`.vars` - Gunakan Perintah Ini UntukGunakan Perintah Ini Untuk
Dapatkan Semua Nama Variabel.

`.vals` - Gunakan Perintah Ini UntukGunakan Perintah Ini Untuk
Dapatkan Semua Nilai Variabel.

**Note:** Jangan Gunakan Perintah Ini
di Grup Publik mana pun.
"""
