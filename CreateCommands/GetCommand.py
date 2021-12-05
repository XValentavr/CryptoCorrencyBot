"""
This module handle /gee command
"""
# project imports
from telebot import types

# local imports
from CreateCommands import StartAndReset
from GetInfoCrypto import Crypto
from BotInit.BotInit import bot_initializer


def create_get_command(message, bot) -> None:
    """
    create buttons when /get is called
    :param message:bot message
    :param bot: bot
    :return: None
    """
    if message.text == '/get':
        bot.send_message(message.chat.id, 'Select one or enter your cryptocurrency')
        # created list which contains to 10 the most popular crypto
        top_crypto = ['BTC', 'ETH', 'ADA', 'BNB', 'SOL', 'XRP', 'LTC', 'DOT', 'LUNA', 'DOGE']
        keyboard = types.InlineKeyboardMarkup()

        # created button from list of crypto
        for value in top_crypto:
            key = types.InlineKeyboardButton(text=value, callback_data=value)
            keyboard.add(key)
        bot.send_message(message.from_user.id, text='There are all buttons!'
                                                    '\nSelect one command to get more info',
                         reply_markup=keyboard)

        # get info about cryptocurrency which typed in the chat by user
        bot.register_next_step_handler(message, handle_text)


def handle_text(message) -> None:
    """
    handle /get command
    :param message: message
    :return: None
    """
    bot = bot_initializer()
    try:
        crypto = message.text
        open_, price, low, close_ = Crypto.pritty_currency(crypto, bot, message)
        # print get info
        currency = f'*Сurrent {crypto.upper()} rate*\nCurrent price is *{close_}* USD\nOpen price is *{open_}* USD\n' \
                   f'high price is *{price}* USD\nlow price is ' \
                   f'*{low}* USD'
        bot.send_message(message.chat.id, currency, parse_mode='Markdown')
        StartAndReset.create_main_buttons(message, bot)

    except TypeError:
        StartAndReset.create_main_buttons(message, bot)


def callback_worker(call, bot) -> None:
    """
    Callback handler if button is pressed'
    :param call: call bot message
    :param bot: bot
    :return: None
    """
    try:
        crypto = call.data
        open_, price, low, close_ = Crypto.pritty_currency(crypto, bot, call)
        # print info which is get
        currency = f'*Сurrent {crypto.upper()} rate*\n\nCurrent price is *{close_}* USD\n\nOpen price is *{open_}* USD\n\n' \
                   f'high price is *{price}* USD\n\nlow price is ' \
                   f'*{low}* USD'
        bot.send_message(call.message.chat.id, currency, parse_mode='Markdown')
    except TypeError:
        StartAndReset.create_main_buttons(call, bot)
