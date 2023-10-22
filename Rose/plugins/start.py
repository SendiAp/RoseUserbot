from pyrogram import Client, filters
from pyrogram.types import Message, ForceReply
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from ..import *
from ..modules.date_info import *
from ..modules.vars import *
from pyrogram import enums

FEEDBACK_REPLY_TEXT = "First please select a bot!!👮"

START_TEXT_CAPTION_TEXT = getenv("START_TEXT_CAPTION_TEXT", None)

FEEDBACK_FINISH_TEXT = "Thanks for your feedback!\n\nYour valuable feedbacks help us to build our bots much friendly. When you sending your feedback please include a screenshot of it because it helps us to decide what is the error.\n\nIt usually takes about 48 hours to get back to you, please accept our apologies in advance for any reply that exceeds this time frame.\n\nFeedback Centre."

SANILA_ASSISTANT_TEXT = "Reporting Area‼️\n\nBot = <a href=https://t.me/sanilaassistant_bot> Sanila's Assistant Bot</a>\n\n" \
                        "◉ Type your report here and send it\n\n" \
                        "◉ After you finish click <<**Finish📩**>>\n\n" \

ADMIN = "1307579425"

FEEDBACK_REPLY_BUTTONS = [
    [
        ("Sanila Assistant Bot🤖💖")
    ],
    [
        ("Song Downloader Bot🤖💖")
    ],
    [
        ("Torrent Downloader Bot🤖💖")
    ],
    [

        ("Telegraph Uploader Bot🤖💖")
    ],
    [
        ("Home 🔙")
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

# START MESSAGE
@bot.on_message(filters.command("start") & filters.private)
async def command1(bot, message):
    text = f"Hello **{message.from_user.first_name}!**"
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
                             f"New User!\n\n◉ User - {message.from_user.first_name}\n◉ Joined time - {date_info.POSTED_TIME}\n◉ Joined date - {date_info.POSTED_DATE}")
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
    tet = f"**<u>Feedback Information</u>**\n\nMessage - `{message.text}`\nWord count - {len(message.text.split())}\nPosted by - {message.from_user.first_name}\nUser ID - {message.from_user.id}\nUsername - @{message.chat.username}\nLanguage - {message.from_user.language_code}\nChat type - {message.chat.type}\n\n<i>*Note: Add more feedbacks or click finish</i>"
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
        bot.send_message(Config.LOG_GROUP_ID, "**New feedback available!**\n\n" + tet, protect_content=True,
                         reply_markup=ForceReply(message.chat.id))
    except Exception as e:
        bot.send_message(message.chat.id,
                         f"**Oops!! error occurred while sending feedback to the admin.**\n\n<i>Reason: {e}</i> ")


@bot.on_message(filters.group & filters.reply & filters.user(ADMIN))
def do_nothing(bot, message):
    try:
        bot.send_message(vaar,
                         f"**Admin message** #admin_msg:\n➖➖➖➖➖➖➖➖➖➖\n{message.text}\n\n~Powered by <a href=https://github.com/sanila2007/Feedback-Bot>Feedback Bot</a>",
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


@bot.on_message(filters.regex(pattern="Sanila Assistant Bot"))
async def reply_to_Assistant(bot, message):
    reply_markup = ForceReply(message.chat.id)
    await bot.send_message(message.chat.id, SANILA_ASSISTANT_TEXT,
                           reply_markup=reply_markup
                           , disable_web_page_preview=True)
