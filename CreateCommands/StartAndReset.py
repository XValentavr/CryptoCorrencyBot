from telebot import types


def create_main_buttons(message, bot):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_searchfor = types.KeyboardButton(text='/get')
    keyboard.add(key_searchfor)

    bot.send_message(message.from_user.id, text='Chose any command',
                     reply_markup=keyboard)
