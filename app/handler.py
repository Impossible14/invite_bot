import asyncio

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from app.log import PHOTO_ID, PHOTO_ALL
import app.keyboard as k

router = Router()

slp = False

choices = {}


@router.message(Command('help'))
async def start(message: Message):
    await message.answer(f'Привет! {message.from_user.full_name}, есть команда /ppgo'
                         '\nнужно отнестись с ответственную вызывая эту команду',
                         reply_markup=k.key_main_2)
    await message.answer()


@router.callback_query(F.data == 'pivo1')
async def start_pp(callback: CallbackQuery):
    user_name = callback.from_user.full_name
    await callback.message.answer_photo(
        photo=PHOTO_ID,
        caption=f"{user_name} подтвердил/а свои серьезные намерения пп \n /ppgo")
    await callback.answer()
    await callback.message.delete()


@router.message(Command('ppgo'))
async def start(message: Message):
    await message.answer(f'Привет! {message.from_user.full_name}',
                         reply_markup=k.key_main)
    await asyncio.sleep(300)


@router.callback_query(F.data == 'pivo')
async def start_pp(callback: CallbackQuery):
    await callback.answer('Молодец ты инициативный!', show_alert=True)
    await callback.message.edit_text('Какое пиво предпочитаете??', reply_markup=await k.pp_func())


@router.callback_query(F.data.startswith('p_'))
async def start_pp(callback: CallbackQuery):
    await callback.answer('Хороший выбор', show_alert=True)
    a = callback.data.split('_')
    choices[callback.from_user.id] = a[1]
    await callback.message.edit_text('Сколько(сложный вопрос)??', reply_markup=await k.pp_func_count())


user_id_all = [508948267, 245035790, 556621757, 426697113]


@router.callback_query(F.data.startswith('c_'))
async def teg(callback: CallbackQuery):
    count_p = callback.data.split('_')
    await callback.answer(f'{count_p[2]}', show_alert=True)
    user_id = callback.from_user.id
    user_name = callback.from_user.full_name
    s = choices[user_id]
    q = []
    p = 0
    for u in user_id_all:
        if u != user_id:
            mention = f'<a href="tg://user?{user_id}">пиво любитель {p}</a>'
            p += 1
            q.append(mention)
    await callback.message.answer_photo(photo=PHOTO_ALL,
                                        caption=f'{user_name} зовет всех пп, '
                                        'нужно обязательно идти'
                                        f'\nсорт: {s}'
                                        f'\nколво: {count_p[1]} л'
                                        f'\n{" ".join(q)}',
                                        parse_mode=ParseMode.HTML)
    await callback.answer()
    await callback.message.delete()
