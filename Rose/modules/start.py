async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if LOG_GROUP_ID:
            Config.ALIVE_LOGO = await bot.send_file(
                LOG_GROUP_ID,
                "https://telegra.ph/file/248b4cd5adb27bf33f15c.jpg",
                caption="**Your RoseUserbot has been started successfully**",
                reply_markup=ReplyKeyboardMarkup(INLINE_BB, one_time_keyboard=False, resize_keyboard=True)
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            message = await bot.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**Ok Bot is Back and Alive.**"
            await bot.edit_message(msg_details[0], msg_details[1], text)
    except Exception as e:
        LOGS.error(e)
        return None
