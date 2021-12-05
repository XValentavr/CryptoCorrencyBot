"""
Thos module creates feedback command handler
"""


def feedback(bot, message) -> None:
    """
    Send message when feedback command is called
    :param bot: telebot
    :param message: message
    """
    bot.send_message(message.chat.id,
                     'For more information, contact @Valentavr. Wishes and claims are expected. Use Eng,'
                     ' Rus,Ukrainian languages')
