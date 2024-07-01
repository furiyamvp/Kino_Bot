from aiogram import types

from loader import dp, _
from mainn.config import ADMINS
from keyboards.default.setting import menu_setting_def


@dp.message_handler(text=["Settings ⚙️", "Настройки ⚙️", "Sozlamalar ⚙️"], chat_id=ADMINS, state="*")
async def settings_menu_handler(message: types.Message):
    text = _("Welcome to the settings menu")
    await message.answer(text=text, reply_markup=await menu_setting_def())



