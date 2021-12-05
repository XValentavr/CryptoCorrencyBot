"""
This module create buttons with top 10 most popular cryptocurrency
"""

# project imports
from telebot import types

# local imports
from BotInit.BotInit import bot_initializer
from CreateCommands import StartAndReset
from Graphs.GetInfoAboutCrypto import send_chart


def generate_graphs_buttons(bot, message) -> None:
    """
    creates buttons with top 10 cryptocurrencies
    :param bot: bot
    :param message: bot message
    """
    if message.text == '/graph':
        top_crypto = ['BTC', 'ETH', 'ADA', 'BNB', 'SOL', 'XRP', 'LTC', 'DOT', 'LUNA', 'DOGE']
        keyboard = types.InlineKeyboardMarkup()
        # created button from list of crypto
        for value in top_crypto:
            key = types.InlineKeyboardButton(text=value, callback_data=value)
            keyboard.add(key)
        bot.send_message(message.from_user.id, text='There are all buttons!'
                                                    '\nSelect one command to get a graph',
                         reply_markup=keyboard)
        # get info about cryptocurrency which typed in the chat by user
        bot.register_next_step_handler(message, handle_text_graph)


def handle_text_graph(message) -> None:
    """
    create buttons and chart
    :param message: bot message
    """
    crypto = message.text
    bot = bot_initializer()
    send_chart(message, crypto)
    StartAndReset.create_main_buttons(message, bot)


def callback_worker(call) -> None:
    """
    send createed chart when command is called
    """
    crypto = call.data
    send_chart(call.message, crypto)
