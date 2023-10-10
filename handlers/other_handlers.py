from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def process_other_command (message: Message):
    await message.answer(text=f"{message.text} я не знаю такой команды обратитесь в /help")
