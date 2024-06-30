from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.admin import admin_main_menu_def
from keyboards.default.back import main_menu_back
from main.config import ADMINS
from states.GivingPremiumState import GivingPremium
from loader import dp, _
from utils.db_commands.update_user_status import admin_update_user_status
from keyboards.inline.change_user_status import admin_change_user_status_def
from utils.db_commands.users import get_user


@dp.message_handler(text=["Giving premium 💎", "Premium berish 💎", "Предоставление премиум 💎"], chat_id=ADMINS,
                    state="*")
async def giving_premium_menu(message: types.Message, state: FSMContext):
    text = _("Please enter user chat id")
    await message.answer(text=text, reply_markup=await main_menu_back())
    await GivingPremium.user_id.set()


@dp.message_handler(state=GivingPremium.user_id, chat_id=ADMINS)
async def admin_change_status_user_handler(message: types.Message, state: FSMContext):
    user = await get_user(int(message.text))
    if user:
        text_template = _("Id: {id}\nChat id: {chat_id}\nStatus: {status}")
        text = text_template.format(id=user['id'], chat_id=user["chat_id"], status=user['status'])
        await state.update_data(user_id=message.text)
        await message.answer(text=text, reply_markup=admin_change_user_status_def)
        await GivingPremium.status.set()
    else:
        text = "People like this chat id"
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
        await state.finish()


@dp.callback_query_handler(state=GivingPremium.status, text="change_premium", chat_id=ADMINS)
async def change_status_free_handler(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()
    user_id = int(date['user_id'])
    if await admin_update_user_status(user_id=user_id, new_value="Premium"):
        text = _("User's status has changed")
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
    else:
        text = "There was an error changing the user's status"
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())


@dp.callback_query_handler(state=GivingPremium.status, text="change_free", chat_id=ADMINS)
async def change_status_premium_handler(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()
    user_id = int(date['user_id'])
    if await admin_update_user_status(user_id=user_id, new_value="Free"):
        text = _("User's status has changed")
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
    else:
        text = "There was an error changing the user's status"
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
