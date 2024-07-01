from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.channels import channels
from loader import dp, _
from mainn.config import ADMINS
from states.Order_movie import OrderMovie
from utils.db_commands.users import get_user_status
from keyboards.default.user import user_main_menu_def
from keyboards.default.user_premium import user_main_menu_def_premium

import random

from utils.misc.subscription import check_subscription


@dp.message_handler(text=["Order a movie 🛍🎥", "Заказать фильм 🛍🎥", "Film buyurtma qilish 🛍🎥"], state="*")
async def user_premium_order_movie_handler(message: types.Message):
    user_status = await get_user_status(int(message.chat.id))
    if await check_subscription(int(message.chat.id)):
        if user_status == "Premium":
            text = _(
                "Requirements: The movie you are looking for must be available, do not use offensive language, and your message must not exceed 100 characters."
                "\nReminder. If you say something bad, we will remove your bonus.")
            await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
            await OrderMovie.text.set()
        else:
            text = "You have not purchased premium, purchase bot premium to use this function"
            await message.answer(text=text, reply_markup=await user_main_menu_def())
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)


@dp.message_handler(state=OrderMovie.text)
async def order_movie_text_handler(message: types.Message, state: FSMContext):
    if len(message.text) < 100:
        await state.update_data(text=message.text)
        admin = random.choice(ADMINS)
        await dp.bot.send_message(chat_id=admin, text=message.text)
        await state.finish()
    else:
        text_template = _("Your message has exceeded 100 characters, you used {len} characters in your message")
        text = text_template.format(len=len(message.text))
        await message.answer(text=text, reply_markup=await user_main_menu_def_premium())
