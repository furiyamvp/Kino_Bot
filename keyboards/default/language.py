from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def change_language_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("English 🇺🇸"),
                KeyboardButton("Русский 🇷🇺"),
            ],
            [
                KeyboardButton("O'zbek 🇺🇿"),
            ]
        ], resize_keyboard=True
    )
    return markup
