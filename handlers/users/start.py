from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.user import user_main_menu_def
from keyboards.default.user_premium import user_main_menu_def_premium
from keyboards.inline.channels import channels
from keyboards.inline.start import all_languages
from loader import dp, _
from states.Register import RegisterState
from utils.db_commands.users import add_user, get_user_status
from utils.misc.subscription import check_subscription


@dp.message_handler(CommandStart(), state="*")
async def user_start_handler(message: types.Message):
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
    else:
        text = "Tilni Tanlang,     select a language,     выберите язык"
        await message.answer(text=text, reply_markup=all_languages)
        await RegisterState.language.set()


@dp.callback_query_handler(state=RegisterState.language)
async def language_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=call.data)
    data = await state.get_data()
    if await add_user(data, call.message):
        text = _(
            "This bot is the bot of the Zangora Ekran channel. In this bot, if you send us the link of the movie you saw on Instagram, we will send you that movie\nFor the bot to start, click /start",
            locale=call.data)
        await call.message.answer(text=text)
        await state.finish()

    else:
        text = _("There is an error in the bot, please contact us", locale=call.data)
        await call.message.answer(text=text)
        await state.finish()
