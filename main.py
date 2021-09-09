from BotInit.BotInit import bot_initializer
from CreateCommands import StartAndReset, Commands, InfoCommand, GetCommand

if __name__ == "__main__":
    crypto = bot_initializer()


    @crypto.message_handler(commands=['help'])
    def show_help(message):
        Commands.create_info_buttons(message, crypto)


    @crypto.message_handler(commands=['start'])
    def send_welcome(message):
        StartAndReset.create_main_buttons(message, crypto)


    @crypto.message_handler(commands=['reset'])
    def send_reset(message):
        StartAndReset.create_main_buttons(message, crypto)


    @crypto.message_handler(commands=['info'])
    def send_reset(message):
        InfoCommand.create_info_button(message, crypto)


    @crypto.message_handler(commands=['get'])
    def send_get(message):
        GetCommand.create_get_command(message, crypto)


    @crypto.callback_query_handler(func=lambda call: True)
    def touch_handler(call):
        Commands.callback_worker(call, crypto)
        GetCommand.callback_worker(call, crypto)


    crypto.polling(none_stop=True, interval=0)
