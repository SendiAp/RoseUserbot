from pyrogram import Client, filters
from pyrogram.types import Message, ForceReply
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from ..import *
from ..modules.date_info import *
from ..modules.vars import *
from pyrogram import enums

FEEDBACK_REPLY_TEXT = "Apa kamu yakin ingin mengirim pesan kepada owner bot ini?"

START_TEXT_CAPTION_TEXT = getenv("START_TEXT_CAPTION_TEXT", None)

FEEDBACK_FINISH_TEXT = "**💬PESAN TERKIRIM!**"

ROSE_ASSISTANT_TEXT = "**❗BERIKAN SAYA PESAN KEPADA BOS SAYA.**\n\n" \
                        ">> Berikan saya pesan teks tidak support dengan media atau sticker, jika sudah lalu klik  **KIRIM📩**" \

ADMIN = var.OWNER_ID

FEEDBACK_REPLY_BUTTONS = [
    [
        ("Yes")
    ],
    [
        ("No")
    ]
]

INLINE_BB = InlineKeyboardMarkup(

    [

        [

            InlineKeyboardButton("Inline Mode Bot list 🔎", switch_inline_query_current_chat="")

        ]

    ]

)

REPLY_BUTTONS = [
    [
        ("Feedbacks 📝"),
        ("Rate Bots ⭐")
    ],
    [
        ("Learn Bots 👨‍🏫"),
        ("Contact 📞")

    ],
    [
        ("About Bot 🤖"),
        ("Changelog ♾️")
    ]
]

FINISH_FEEDBACK_BUTTONS = [
    [
        ("Finish📩")
    ]
]

# START MESSAGE
@bot.on_message(filters.command("start") & filters.private)
async def command1(bot, message):
    text = START_TEXT_CAPTION_TEXT
    reply_markup = INLINE_BB
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    await message.reply(
        "Use ReplyKeyboard or Inline Mode...",
        reply_markup=ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    )
    try:
        await bot.send_message(Config.LOG_GROUP_ID,
                             f"**🆕PENGGUNA BARU!**\n\n◉ Nama: {message.from_user.first_name}\n◉ Bot: {self.bot.mention}")
    except Exception as er:
        print(f"Unable to send the logs to the channel.\nReason: {er}")


@bot.on_message(filters.regex(pattern="Feedbacks"))
def reply_to_Feedback(bot, message):
    text = FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.reply & filters.private)
def fbb(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    tet = f"**🆕PESAN BARU!**\n\n• Jumlah: {len(message.text.split())}\n• Nama: {message.from_user.first_name}\n• UseID: {message.from_user.id}\n• Username: @{message.chat.username}\n• Bahasa: {message.from_user.language_code}\n• Type: {message.chat.type}\n\n {message.text}"
    reply_markup = ReplyKeyboardMarkup(FINISH_FEEDBACK_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=tet,
        reply_markup=reply_markup,
        quote=True,
        protect_content=True
    )
    global vaar
    vaar = message.chat.id
    try:
        bot.send_message(Config.LOG_GROUP_ID, "• Bot: {self.bot.mention}\n\n" + tet, protect_content=True,
                         reply_markup=ForceReply(message.chat.id))
    except Exception as e:
        bot.send_message(message.chat.id,
                         f"**Oops!! error occurred while sending feedback to the admin.**\n\n<i>Reason: {e}</i> ")


@bot.on_message(filters.group & filters.reply & filters.user(ADMIN))
def do_nothing(bot, message):
    try:
        bot.send_message(vaar,
                         f"**Admin message** #admin_msg:\n➖➖➖➖➖➖➖➖➖➖\n{message.text}\n\n~Powered by: Rose Userbot",
                         disable_web_page_preview=True, protect_content=True)
        bot.send_message(Config.LOG_GROUP_ID, f"Your reply have been sent to the user successfully.",
                         protect_content=True)
    except Exception as error_nothing:
        print(f"Error occurred: {error_nothing}")

@bot.on_message(filters.regex(pattern="Finish"))
def reply_finish(bot, message):
    bot.send_message(message.chat.id, FEEDBACK_FINISH_TEXT,
                     reply_markup=ReplyKeyboardMarkup(REPLY_BUTTONS, resize_keyboard=True,
                                                      one_time_keyboard=False))


@bot.on_message(filters.regex(pattern="Yes"))
async def reply_to_Assistant(bot, message):
    reply_markup = ForceReply(message.chat.id)
    await bot.send_message(message.chat.id, ROSE_ASSISTANT_TEXT,
                           reply_markup=reply_markup
                           , disable_web_page_preview=True)
