from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.channels import channels
from loader import dp, _
from keyboards.default.language import change_language_def
from states.Change_language import ChangeLanguage
from utils.db_commands.users import get_user, update_user_language
from utils.misc.subscription import check_subscription


@dp.message_handler(text=["Change language 🇺🇿🇷🇺🇺🇸", "Изменить язык 🇺🇿🇷🇺🇺🇸", "Tilni o'zgartirish 🇺🇿🇷🇺🇺🇸"], state="*")
async def change_language_handler(message: types.Message):
    if await check_subscription(int(message.chat.id)):
        text = _("select any language to change the language")
        await message.answer(text=text, reply_markup=await change_language_def())
        await ChangeLanguage.language.set()
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)


@dp.message_handler(state=ChangeLanguage.language, text="English 🇺🇸")
async def change_language_en_handler(message: types.Message, state: FSMContext):
    user = await get_user(int(message.chat.id))
    if user["language"] == "en":
        text = _("You are currently using this language")
        await message.answer(text=text)
        await ChangeLanguage.language.set()
    else:
        change_language = await update_user_language(chat_id=message.chat.id, language="en")
        if change_language is True:
            text = _("The language has changed\nclick /start for the bot", locale=user["language"])
            await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
            await state.finish()


@dp.message_handler(state=ChangeLanguage.language, text="Русский 🇷🇺")
async def change_language_ru_handler(message: types.Message, state: FSMContext):
    user = await get_user(int(message.chat.id))
    if user["language"] == "ru":
        text = _("You are currently using this language")
        await message.answer(text=text)
        await ChangeLanguage.language.set()
    else:
        change_language = await update_user_language(chat_id=message.chat.id, language="ru")
        if change_language is True:
            text = _("The language has changed\nclick /start for the bot", locale=user["language"])
            await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
            await state.finish()


@dp.message_handler(state=ChangeLanguage.language, text="O'zbek 🇺🇿")
async def change_language_uz_handler(message: types.Message, state: FSMContext):
    user = await get_user(int(message.chat.id))
    if user["language"] == "uz":
        text = _("You are currently using this language")
        await message.answer(text=text)
        await ChangeLanguage.language.set()
    else:
        change_language = await update_user_language(chat_id=message.chat.id, language="uz")
        if change_language is True:
            text = _("The language has changed\nclick /start for the bot", locale=user["language"])
            await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
            await state.finish()
