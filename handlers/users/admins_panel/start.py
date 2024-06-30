from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.admin import admin_main_menu_def
from keyboards.inline.channels import channels
from keyboards.inline.start import all_languages
from loader import dp, _
from main.config import ADMINS
from states.Register import RegisterStateAdmin
from utils.db_commands.users import get_user
from utils.db_commands.users import add_admin_table_user


@dp.message_handler(CommandStart(), chat_id=ADMINS, state="*")
async def admin_start_handler(message: types.Message):
    if await get_user(int(message.chat.id)):
        text = _("Hello Admin🫡")
        await message.answer(text=text, reply_markup=await admin_main_menu_def())
    else:
        text = "Tilni Tanlang,     select a language,     выберите язык"
        await message.answer(text=text, reply_markup=all_languages)
        await RegisterStateAdmin.language.set()


@dp.callback_query_handler(state=RegisterStateAdmin.language)
async def language_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data)
    data = await state.get_data()
    if await add_admin_table_user(data, call.message):
        text = _("This bot is the bot of the Zangora Ekran channel. In this bot, if you send us the link of the movie you saw on Instagram, we will send you that movie\nFor the bot to start, click /start",
                 locale=call.data)
        await call.message.answer(text=text)
        await state.finish()

    else:
        text = _("There is an error in the bot, please contact us", locale=call.data)
        await call.message.answer(text=text)
        await state.finish()
