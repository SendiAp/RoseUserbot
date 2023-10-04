
import os

from pyrogram import *
from pyrogram.types import *

from ..modules.basic import edit_or_reply, get_text, get_user

from ..import *

OWNER = os.environ.get("OWNER", "Rose-Userbot🌹")
BIO = os.environ.get("BIO", "404 : Bio Lost")


@app.on_message(commandx(["clone"]) & SUDOERS)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await edit_or_reply(message, "`Cloning`")
    userk = get_user(message, text)[0]
    user = await client.get_users(user_id)
    if not user:
        await op.edit("`Siapa yang harus saya tiru:(`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user.photo.big_file_id if user.photo else None
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**From now I'm** __{f_name}__")


@app.on_message(commandx(["revert"]) & SUDOERS)
async def revert(client, message):
    await message.edit("`Reverting`")
    r_bio = BIO

    # Get ur Name back
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )

    # Delte first photo to get ur identify
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`I am back!`")

__NAME__ = "clone"
__MENU__ = f"""
**🥀 Clone pengguna.**

`.clone` - **To Clone someone Profile.**

`.revert` - **To Get Your Account Back.**

© Rose Userbot
"""
