from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def main_menu_back():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(_("Back ⬅️"))
            ]
        ], resize_keyboard=True
    )
    return markup
