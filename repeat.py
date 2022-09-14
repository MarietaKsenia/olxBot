from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bot_keyboards import (first_start_keyboard, menu_keyboard)



TOKEN = '5669721003:AAHm1uNSZyJXRw43GZH84cvwTXsmjD833zY'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я ОЛХ бот, Привет,{msg.from_user.first_name}',
                     reply_markup=first_start_keyboard())


@dp.message_handler(lambda message: message.text == 'Отримати підписку')
async def start_info(message: types.Message):
    await  bot.send_message(
        message.from_user.id, ''''В якості ознайомлення з ботом, 
        вам <b>Безкоштовний доступ</b> пошук за 1 посиланням
        Для того, щоб скористатися  сервісом необхідно:
        1)Сформувати пошук на сайті <b>OLX</b>
        2)Натиснути кнопку "Додати посилання"
        3)Відправити посилання в повідомленні нижче''',
        reply_markup=menu_keyboard(),
        parse_mode='HTML'
    )

@dp.message_handler(lambda message: message.text == 'Отримати підписку')
async  def add_new_olx_link(message: types.Message):
    await  bot.send_message(
        message.from_user.id,
        'Введіть посилання'
    )

@dp.message_handler(content_types=['text'])
async def add_link_step_2(message: types.Message):
    print('t')
    link = message.text.lower()

#
# @dp.message_handler(content_types=['text'])
# async def get_text_messages(msg: types.Message):
#     if msg.text.lower() == 'привет':
#         await msg.answer('Привет!')
#     else:
#         await msg.answer('Моя твоя не понимать!!!(')


if __name__ == '__main__':
    executor.start_polling(dp)