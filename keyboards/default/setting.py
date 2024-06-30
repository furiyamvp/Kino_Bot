from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def menu_setting_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(_("Change language 🇺🇿🇷🇺🇺🇸"))
            ]
        ], resize_keyboard=True
    )
    return markup
