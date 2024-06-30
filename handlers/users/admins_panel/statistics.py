from aiogram import types

from loader import dp, _
from main.config import ADMINS
from keyboards.default.admin import statistics_menu_def
from utils.db_commands.statictics import quantity_users, quantity_films


@dp.message_handler(text=["Statistics 📊", "Статистикы 📊", "Statistikalar 📊"], chat_id=ADMINS, state="*")
async def statistics_menu_handler(message: types.Message):
    text = _("Welcome to the statistics menu")
    await message.answer(text=text, reply_markup=await statistics_menu_def())


@dp.message_handler(text=["Quantity users 👥", "Количество пользователей 👥", "Foydalanuvchilar soni 👥"], chat_id=ADMINS, state="*")
async def quantity_user_menu_handler(message: types.Message):
    quantity_user = await quantity_users()
    quantity_user_number = quantity_user["count_1"]
    text = f"Bot is used by {quantity_user_number} people"
    await message.answer(text=text, reply_markup=await statistics_menu_def())


@dp.message_handler(text=["Quantity films 🎥", "Количественные фильмы 🎥", "Filmlar soni 🎥"], chat_id=ADMINS, state="*")
async def quantity_film_menu_handler(message: types.Message):
    quantity_film = await quantity_films()
    quantity_film_number = quantity_film["count_1"]
    text = f"Bot has {quantity_film_number}  films"
    await message.answer(text=text, reply_markup=await statistics_menu_def())
