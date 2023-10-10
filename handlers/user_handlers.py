from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import game_keyboard, start_keyboard
from services.services import random_jest

router = Router()

@router.message(CommandStart())
async def process_start_command (message: Message):
    await message.answer(text=LEXICON_RU["/start"],
                         reply_markup = start_keyboard)

@router.message(Command(commands="help"))
async def process_help_command (message: Message):
    await message.answer(text=LEXICON_RU["/help"])

@router.message(F.text.in_("Давай!"))
async def process_lets_go_command (message: Message):
    await message.answer(text=LEXICON_RU["Давай!"],
                         reply_markup=game_keyboard)

@router.message(F.text.in_("Не хочу!"))
async def process_cancel_command (message: Message):
    await message.answer(text=LEXICON_RU["Не хочу!"])

@router.message(F.text.in_(["бумага", "камень", "ножницы"]))
async def process_game_command (message: Message):
    answer = random_jest(message.text)
    await message.answer(text=f'мой выбор {answer[1]}. Результат {answer[0]}. Хочешь сыграть еще? Жми на клавитауре:',
                         reply_markup = start_keyboard)
