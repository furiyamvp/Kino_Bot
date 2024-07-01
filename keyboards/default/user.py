from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def user_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(_("Call center 📞")),
            ]
        ], resize_keyboard=True
    )
    return markup
