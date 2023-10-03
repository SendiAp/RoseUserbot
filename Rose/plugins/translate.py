from py_trans import Async_PyTranslator
from gpytranslate import Translator
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from ..modules.tools import get_arg
from ..modules.basic import edit_or_reply

from ..import *


@app.on_message(commandx(["tr"]) & SUDOERS)
async def translate(client, message):
  tr_msg = await message.edit("`Processing...`")
  r_msg = message.reply_to_message
  args = get_arg(message)
  if r_msg:
    if r_msg.text:
      to_tr = r_msg.text
    else:
      return await tr_msg.edit("`Mohon Balas Ke Pesan..`")
    # Checks if dest lang is defined by the user
    if not args:
      return await tr_msg.edit(f"`Gunakan tr <kode_bahasa> <kata> atau tr id <balas ke pesan>`")
    # Setting translation if provided
    else:
      sp_args = args.split(" ")
      if len(sp_args) == 2:
        dest_lang = sp_args[0]
        tr_engine = sp_args[1]
      else:
        dest_lang = sp_args[0]
        tr_engine = "google"
  elif args:
    # Splitting provided arguments in to a list
    a_conts = args.split(None, 2)
    # Checks if translation engine is defined by the user
    if len(a_conts) == 3:
      dest_lang = a_conts[0]
      tr_engine = a_conts[1]
      to_tr = a_conts[2]
    else:
      dest_lang = a_conts[0]
      to_tr = a_conts[1]
      tr_engine = "google"
  # Translate the text
  py_trans = Async_PyTranslator(provider=tr_engine)
  translation = await py_trans.translate(to_tr, dest_lang)
  # Parse the translation message
  if translation["status"] == "success":
    tred_txt = f"""
**Translation Engine**: `{translation["engine"]}`
**Translated to:** `{translation["dest_lang"]}`
**Translation:**
`{translation["translation"]}`
"""
    if len(tred_txt) > 4096:
      await tr_msg.edit("`Teks yang anda berikan terlalu panjang, ini bisa memakakan waktu`\n`Tunggu sebentar..`")
      tr_txt_file = open("translated.txt", "w+")
      tr_txt_file.write(tred_txt)
      tr_txt_file.close()
      await tr_msg.reply_document("ptranslated_NEXAUB.txt")
      os.remove("ptranslated.txt")
      await tr_msg.delete()
    else:
      await tr_msg.edit(tred_txt)


__NAME__ = "translate"
__MENU__ = f"""
**🥀 Menerjemahkan bahasa asing.**

`.tr` [kode bahasa] - **Menerjemahkan teks ke bahasa yang disetel. .**

(Default kode bahasa indonesia)

© Rose Userbot
"""
