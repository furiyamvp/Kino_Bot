from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def admin_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(_("Statistics 📊")),
                KeyboardButton(_("Settings ⚙️"))
            ],
            [
                KeyboardButton(_("Giving premium 💎"))
            ],
            [
                KeyboardButton(_("Add Film ➕"))
            ],
        ], resize_keyboard=True
    )
    return markup


async def statistics_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(_("Quantity users 👥")),
                KeyboardButton(_("Quantity films 🎥"))
            ],
            [
                KeyboardButton(_("Back ⬅️"))
            ],
        ], resize_keyboard=True
    )
    return markup
