"""
Create buttons to manipulate a bot using commands
"""
# project imports
from telebot import types


def create_info_buttons(message, bot) -> None:
    """
    creates inline keybort with handle data
    :param message: bot message
    :param bot: telebot
    """
    keyboard = types.InlineKeyboardMarkup()

    key_start = types.InlineKeyboardButton(text='/start', callback_data='start')
    key_help = types.InlineKeyboardButton(text='/help', callback_data='help')
    key_info_first = types.InlineKeyboardButton(text='/info', callback_data='info')
    key_info_reset = types.InlineKeyboardButton(text='/reset', callback_data='reset')
    key_info_feedback = types.InlineKeyboardButton(text='/feedback', callback_data='feedback')

    keyboard.add(key_start)
    keyboard.add(key_help)
    keyboard.add(key_info_first)
    keyboard.add(key_info_reset)
    keyboard.add(key_info_feedback)

    bot.send_message(message.from_user.id, text='There are all buttons!'
                                                '\nSelect one command to get more info',
                     reply_markup=keyboard)


def callback_worker(call, bot) -> None:
    """
    Create handler to check commands and do something
    :param call: message to handle
    :param bot: telebot
    """

    if call.data == 'help':
        bot.send_message(call.message.chat.id, 'This command can help you to get more info about command posibilities')
    if call.data == 'start':
        bot.send_message(call.message.chat.id, 'Starting bot')
    if call.data == 'info':
        bot.send_message(call.message.chat.id, 'Get bot posibilities')
    if call.data == 'reset':
        bot.send_message(call.message.chat.id, 'Back to start')
    if call.data == 'feedback':
        bot.send_message(call.message.chat.id, 'Contact with developer')
