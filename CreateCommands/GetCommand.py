from CreateCommands import StartAndReset
from GetInfoCrypto import Crypto


def create_get_command(message, bot):
    bot.send_message(message.chat.id, 'Enter cryptocurrency')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        try:
            crypto = message.text
            a, b, c, d = Crypto.pritty_currency(crypto, bot, message)
            currency = f'Open price is *{a}*\nhigh price is *{b}*\nlow price is *{c}*\nclose price is *{d}*'
            bot.send_message(message.chat.id, currency, parse_mode='Markdown')
        except TypeError:
            StartAndReset.create_main_buttons(message, bot)
