from aiogram import types


def first_start_keyboard():
    pool_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pool_keyboard.add(types.KeyboardButton(text = 'Отримати підписку'))
    pool_keyboard.add(types.KeyboardButton(text='Про бота ℹ️ '))
    pool_keyboard.add(types.KeyboardButton(text='Відміна 🚫'))
    return  pool_keyboard


def menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Додати посилання ➕'))
    keyboard.add(types.KeyboardButton(text='Видалити посилання ➖'))
    keyboard.add(types.KeyboardButton(text='Зупинити бота 🚫'))
    return  keyboard