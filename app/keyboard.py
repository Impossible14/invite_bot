from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


key_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пиво пить, хочу позвать', callback_data='pivo')]
])

key_main_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я буду ответственный', callback_data='pivo1')]
])


pp = ['p_светлое', 'p_темное', 'p_и светлое и темное..']


async def pp_func():
    keyboard = InlineKeyboardBuilder()
    for p in pp:
        a = p.split('_')
        keyboard.add(InlineKeyboardButton(text=a[1], callback_data=f'{p}'))
    return keyboard.adjust(2).as_markup()


p_count = ['c_0,5_для хорошего сна', 'c_1_нормис', 'c_2_серезно', 'c_3_ты крейзи']


async def pp_func_count():
    keyboard = InlineKeyboardBuilder()
    for p_c in p_count:
        a = p_c.split('_')
        keyboard.add(InlineKeyboardButton(text=f'{a[1]} л', callback_data=f'{p_c}'))
    return keyboard.adjust(2).as_markup()
