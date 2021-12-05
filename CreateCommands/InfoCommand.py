"""
This module creates imfo handler command
"""


def create_info_button(message, bot) -> None:
    """
    if command is help then show information about possibilities
    :param message: bot message
    :param bot: bot
    :return: None
    """
    try:
        bot.send_message(message.chat.id, 'This bot will allow you to follow the current cryptocurrency rates')
    except Exception:
        print('Something get wrong. Try again')
