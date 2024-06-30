from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.user import user_main_menu_def
from keyboards.default.user_premium import user_main_menu_def_premium
from keyboards.inline.channels import channels
from loader import dp, _
from utils.db_commands.users import get_user_status
from utils.misc.subscription import check_subscription


@dp.message_handler(text=["Back ⬅️", "Назад ⬅️", "Orqaga ⬅️"], state="*")
async def user_back_main_menu_handler(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    if await get_user_status(user_id) == "Free":
        if await check_subscription(int(user_id)):
            text = _("Welcome to the Telegram Bot")
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            await message.reply(
                _("You have not subscribed to the channels!\n"
                  "After subscribing, press /start to activate the bot."),
                reply_markup=channels)
    elif await get_user_status(int(message.chat.id)) == "Premium":
        if await check_subscription(int(user_id)):
            text = _("Welcome to the Telegram Bot")
            await message.answer(text=text, reply_markup=await user_main_menu_def_premium())
        else:
            await message.reply(
                _("You have not subscribed to the channels!\n"
                  "After subscribing, press /start to activate the bot."), reply_markup=channels)
