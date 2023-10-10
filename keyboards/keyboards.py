from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

kb_builder = ReplyKeyboardBuilder()

rock_btn = KeyboardButton (text = "камень")
paper_btn = KeyboardButton (text = "бумага")
scissors_btn = KeyboardButton (text = "ножницы")

yes_btn = KeyboardButton (text = "Давай!")
no_btn = KeyboardButton (text = "Не хочу!")

kb_builder.row (rock_btn, paper_btn, scissors_btn)
game_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize = True, one_time_keyboard=True)

kb_builder = ReplyKeyboardBuilder()

kb_builder.row (yes_btn, no_btn)
start_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize = True, one_time_keyboard=True)