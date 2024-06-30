from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def user_main_menu_def_premium():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(_("Change language 🇺🇿🇷🇺🇺🇸")),
                KeyboardButton(_("Order a movie 🛍🎥")),
            ],
            [
                KeyboardButton(_("Call center 📞")),
            ]
        ], resize_keyboard=True
    )
    return markup
