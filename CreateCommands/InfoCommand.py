def create_info_button(message, bot):
    try:
        bot.send_message(message.chat.id, 'This bot will allow you to follow the current cryptocurrency rates')
    except Exception:
        print('Something get wrong. Try again')
