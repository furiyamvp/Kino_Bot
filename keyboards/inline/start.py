from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

all_languages = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek 🇺🇿", callback_data="uz"),
            InlineKeyboardButton(text="English 🇺🇸", callback_data="en"),
            InlineKeyboardButton(text="Русский 🇷🇺", callback_data="ru")

        ]
    ]
)
