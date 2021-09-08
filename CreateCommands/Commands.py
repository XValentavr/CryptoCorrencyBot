from telebot import types


def create_info_buttons(message, bot):
    keyboard = types.InlineKeyboardMarkup()

    key_start = types.InlineKeyboardButton(text='/start', callback_data='start')
    key_help = types.InlineKeyboardButton(text='/help', callback_data='help')
    key_info_first = types.InlineKeyboardButton(text='/info', callback_data='info')
    key_info_reset = types.InlineKeyboardButton(text='/reset', callback_data='reset')

    keyboard.add(key_start)
    keyboard.add(key_help)
    keyboard.add(key_info_first)
    keyboard.add(key_info_reset)

    bot.send_message(message.from_user.id, text='There are all buttons!'
                                                '\nSelect one command to get more info',
                     reply_markup=keyboard)


def callback_worker(call, bot):
    if call.data == 'help':
        bot.send_message(call.message.chat.id, 'This command can help you to get more info about command posibilities')
    if call.data == 'start':
        bot.send_message(call.message.chat.id, 'Starting bot')
    if call.data == 'info':
        bot.send_message(call.message.chat.id, 'Get bot posibilities')
    if call.data == 'reset':
        bot.send_message(call.message.chat.id, 'Back to start')
