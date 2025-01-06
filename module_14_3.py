import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


from config import *
from keyboards import *
import texts
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()           #возраст
    growth = State()        #рост
    weight = State()        # вес


@dp.message_handler(text=['Рассчитать'])
async def send_inline_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        '10·вес + 6.25·рост – 5·возраст + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        await state.update_data(age=float(message.text))
    except ValueError:
        await message.answer('Введите свой возраст:')
        await UserState.age.set()
    else:
        await message.answer('Введите свой рост:')
        await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        await state.update_data(growth=float(message.text))
    except ValueError:
        await message.answer('Введите свой рост:')
        await UserState.growth.set()
    else:
        await message.answer('Введите свой вес:')
        await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        await state.update_data(weight=float(message.text))
    except ValueError:
        await message.answer('Введите свой вес:')
        await UserState.weight.set()
    else:
        data = await state.get_data()
        # Resting energy expenditure
        REE = 10 * data['weight'] \
            + 6.25 * data['growth'] \
            - 5 * data['age'] + 5
        await message.answer(
            f'Ваша суточная норма {round(REE, 2)} килокалорий')
        await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f"Привет! " + texts.start, reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer(
        'Данный бот подсчитывает норму потребления калорий по'
        ' упрощённой формуле Миффлина - Сан Жеора'
        ' (https://www.calc.ru/Formula-Mifflinasan-Zheora.html).')


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    await message.answer('У вас есть возможность приобрести следующие товары:')
    with open("file/A.png", "rb") as img_A:
        await message.answer_photo(img_A, 'Название: Product_1 | Описание: Самый лучший комплекс A| Цена: 100')
    with open("file/B.png", "rb") as img_B:
        await message.answer_photo(img_B, 'Название: Product_2 | Описание: Самый лучший комплекс B| Цена: 200')
    with open("file/C.png", "rb") as img_C:
        await message.answer_photo(img_C, 'Название: Product_3 | Описание: Самый лучший комплекс C| Цена: 300')
    with open("file/D.png", "rb") as img_D:
        await message.answer_photo(img_D, 'Название: Product_4 | Описание: Самый лучший комплекс D| Цена: 400')
    await message.answer('Для покупки товара нажмите на соответствующую кнопку',reply_markup=goods_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)