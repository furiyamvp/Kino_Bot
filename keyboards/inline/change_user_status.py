from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _

admin_change_user_status_def = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=_("Change free 🆓"), callback_data="change_free"),
            InlineKeyboardButton(text=_("Change premium 💎"), callback_data="change_premium"),
        ],
        [
            InlineKeyboardButton(text=_("Back ⬅️"), callback_data="admin_back"),
        ]
    ]
)
