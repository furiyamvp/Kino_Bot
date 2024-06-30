from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import admin_main_menu_def
from main.config import ADMINS
from loader import dp, _


@dp.message_handler(text=["Back ⬅️", "Назад ⬅️", "Orqaga ⬅️"], chat_id=ADMINS, state="*")
async def stickers_menu(message: types.Message, state: FSMContext):
    text = _("Welcome to the main menu")
    await message.answer(text=text, reply_markup=await admin_main_menu_def())
    await state.finish()
