"""
This module creates main command that can find info about crypto
"""

# project imports
from telebot import types


def create_main_buttons(message, bot) -> None:
    """
    create main command
    :param message: bot message
    :param bot: bot
    :return: None
    """
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_searchfor = types.KeyboardButton(text='/get')
    keyboard.add(key_searchfor)
    key_graph = types.KeyboardButton(text='/graph')
    keyboard.add(key_graph)
    bot.send_message(message.from_user.id, text='Chose any command',
                     reply_markup=keyboard)
