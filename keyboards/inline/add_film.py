from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _
add_film_status = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Free 🆓"), callback_data="Free"),
            InlineKeyboardButton(text=_("Premium 💎"), callback_data="Premium"),
        ]
    ]
)


add_film_confirmation: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="Add"),
            InlineKeyboardButton(text="❌", callback_data="Not_add"),
        ]
    ]
)

