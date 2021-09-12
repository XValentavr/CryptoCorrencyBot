from CreateCommands import StartAndReset
from GetInfoCrypto import Crypto
from telebot import types


def create_get_command(message, bot):
    bot.send_message(message.chat.id, 'Select one or enter your cryptocurrency')
    top_crypto = ['BTC', 'ETH', 'ADA', 'BNB', 'SOL', 'XRP', 'LTC', 'DOT', 'LUNA', 'DOGE']
    keyboard = types.InlineKeyboardMarkup()
    for value in top_crypto:
        key = types.InlineKeyboardButton(text=value, callback_data=value)
        keyboard.add(key)
    bot.send_message(message.from_user.id, text='There are all buttons!'
                                                '\nSelect one command to get more info',
                     reply_markup=keyboard)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        try:
            crypto = message.text
            open_, price, low, close_ = Crypto.pritty_currency(crypto, bot, message)
            currency = f'*Сurrent {crypto.upper()} rate*\nCurrent price is *{close_}* USD\nOpen price is *{open_}* USD\n' \
                       f'high price is *{price}* USD\nlow price is ' \
                       f'*{low}* USD'
            bot.send_message(message.chat.id, currency, parse_mode='Markdown')
        except TypeError:
            StartAndReset.create_main_buttons(message, bot)


def callback_worker(call, bot):
    try:
        crypto = call.data
        open_, price, low, close_ = Crypto.pritty_currency(crypto, bot, call)
        currency = f'*Сurrent {crypto.upper()} rate*\n\nCurrent price is *{close_}* USD\n\nOpen price is *{open_}* USD\n\n' \
                   f'high price is *{price}* USD\n\nlow price is ' \
                   f'*{low}* USD'
        bot.send_message(call.message.chat.id, currency, parse_mode='Markdown')
    except TypeError:
        StartAndReset.create_main_buttons(call, bot)
