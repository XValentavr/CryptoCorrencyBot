"""
Main file starting the bot and all handlers
"""

# local imports
from BotInit.BotInit import bot_initializer
from CreateCommands import StartAndReset, Commands, InfoCommand, GetCommand, FeedBack
from Graphs import GenerateButtons

if __name__ == "__main__":
    crypto = bot_initializer()


    @crypto.message_handler(commands=['help'])
    def show_help(message):
        """
        creates help command handler
        """
        Commands.create_info_buttons(message, crypto)


    @crypto.message_handler(commands=['feedback'])
    def feedback(message):
        """
        creates feedback command handler
        """
        FeedBack.feedback(crypto, message)


    @crypto.message_handler(commands=['start'])
    def send_welcome(message):
        """
        creates start command handler
        """
        StartAndReset.create_main_buttons(message, crypto)


    @crypto.message_handler(commands=['reset'])
    def send_reset(message):
        """
        creates reset command handler
        """
        StartAndReset.create_main_buttons(message, crypto)


    @crypto.message_handler(commands=['info'])
    def send_reset(message):
        """
        creates info command handler
        """
        InfoCommand.create_info_button(message, crypto)


    @crypto.message_handler(commands=['get'])
    def send_get(message):
        """
        creates get command handler
        """
        GetCommand.create_get_command(message, crypto)


    @crypto.message_handler(commands=['graph'])
    def send_get_graph(message):
        """
        creates graph command handler
        """
        GenerateButtons.generate_graphs_buttons(crypto, message)


    @crypto.callback_query_handler(func=lambda call: True)
    def touch_handler(call):
        """
        creates handler when touch buttons
        """
        Commands.callback_worker(call, crypto)
        GetCommand.callback_worker(call, crypto)
        GenerateButtons.callback_worker(call)


    # start nonstop bot
    crypto.polling(none_stop=True, interval=0)
