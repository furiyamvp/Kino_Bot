from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.admin import admin_main_menu_def
from keyboards.inline.add_film import add_film_status, add_film_confirmation
from mainn.config import ADMINS

from loader import dp, _
from states.AddFilmState import AddFilm
from keyboards.default.back import main_menu_back
from utils.checker.checker_link import check_link_instagram, check_link_tiktok, check_link_you_tube
from utils.db_commands.film import add_film, get_film_film


@dp.message_handler(text=["Add Film ➕", "Добавить фильм ➕", "Film qo'shish ➕"], state="*", chat_id=ADMINS)
async def add_product_handler(message: types.Message):
    text = _("Please upload the movie to the bot")
    await message.answer(text=text, reply_markup=await main_menu_back())
    await AddFilm.film.set()


@dp.message_handler(state=AddFilm.film, chat_id=ADMINS, content_types=types.ContentType.VIDEO)
async def add_product_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(film=message.video.file_id)
    await state.update_data(quality=message.video.height)
    text = _("Please enter a movie title.\n"
             "Example: Harry Potter")
    await message.answer(text=text)
    await AddFilm.name.set()


@dp.message_handler(state=AddFilm.film)
async def error_photo_handler(message: types.Message):
    text = _("You can only upload videos, you cannot upload anything in text format.")
    await message.answer(text=text)
    await AddFilm.film.set()


@dp.message_handler(state=AddFilm.name, chat_id=ADMINS)
async def add_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    text = _("Please enter the country in which the movie was released\n"
             "Example: USA")
    await message.answer(text=text)
    await AddFilm.state.set()


@dp.message_handler(state=AddFilm.state, chat_id=ADMINS)
async def add_state_handler(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(state=message.text)
        text = _("Please enter year the movie was released\n"
                 "Example: 2024")
        await message.answer(text=text)
        await AddFilm.date.set()
    else:
        text = _("Please do not use numbers")
        await message.answer(text=text)
        await AddFilm.state.set()


@dp.message_handler(state=AddFilm.date, chat_id=ADMINS)
async def add_date_handler(message: types.Message, state: FSMContext):
    if message.text.isnumeric():
        await state.update_data(date=message.text)
        text = _("Please enter the movie type\n"
                 "Example: Fight")
        await message.answer(text=text)
        await AddFilm.type.set()
    else:
        text = _("Please do not use letter")
        await message.answer(text=text)
        await AddFilm.date.set()


@dp.message_handler(state=AddFilm.type, chat_id=ADMINS)
async def add_type_handler(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)
    text = _("Please enter film's link on instagram \n"
             "Example: https://www.instagram.com/******")
    await message.answer(text=text)
    await AddFilm.instagram.set()


@dp.message_handler(state=AddFilm.instagram, chat_id=ADMINS)
async def add_instagram_link_handler(message: types.Message, state: FSMContext):
    if await check_link_instagram(message.text):
        await state.update_data(instagram=message.text)
        text = _("Please enter film's link on tiktok\n"
                 "Example: https://vt.tiktok.com/******")
        await message.answer(text=text)
        await AddFilm.tiktok.set()
    else:
        text = _("you can only enter an instagram link")
        await message.answer(text=text)
        await AddFilm.instagram.set()


@dp.message_handler(state=AddFilm.tiktok, chat_id=ADMINS)
async def add_tiktok_link_handler(message: types.Message, state: FSMContext):
    if await check_link_tiktok(message.text):
        await state.update_data(tiktok=message.text)
        text = _("Please enter film's link on tiktok\n"
                 "Example: https://www.youtube.com/******")
        await message.answer(text=text)
        await AddFilm.you_tube.set()
    else:
        text = _("you can only enter an tiktok link")
        await message.answer(text=text)
        await AddFilm.tiktok.set()


@dp.message_handler(state=AddFilm.you_tube, chat_id=ADMINS)
async def add_you_tube_link_handler(message: types.Message, state: FSMContext):
    if await check_link_you_tube(message.text):
        await state.update_data(you_tube=message.text)
        text = _("Please enter movie status\n"
                 "Example: Free or Premium")
        await message.answer(text=text, reply_markup=add_film_status)
        await AddFilm.status.set()
    else:
        text = _("you can only enter an tiktok link")
        await message.answer(text=text)
        await AddFilm.you_tube.set()


@dp.callback_query_handler(state=AddFilm.status, text="Premium", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    text = "Add the movie to the bot ? ➕"
    await state.update_data(status="Premium")
    await call.message.answer(text=text, reply_markup=add_film_confirmation)
    await AddFilm.confirmation.set()


@dp.callback_query_handler(state=AddFilm.status, text="Free", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    text = "Add the movie to the bot ? ➕"
    await state.update_data(status="Free")
    await call.message.answer(text=text, reply_markup=add_film_confirmation)
    await AddFilm.confirmation.set()


@dp.callback_query_handler(state=AddFilm.confirmation, text="Add", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()
    if await add_film(date):
        film_code = await get_film_film(date["film"])
        text = _("Movie added. ✅")

        caption_template = _("🆔Film's code: {code}\n🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀Quality: {quality}\n"
                             "🌍State: {state}\n📅Date: {date}-year\n🎞️Type: {type}\n💜Instagram: {instagram}\n"
                             "🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}")

        caption = caption_template.format(code=film_code['code'], name=date['name'], quality=date['quality'],
                                          state=date['state'], date=date['date'], type=date['type'],
                                          instagram=date["instagram"], tiktok=date["tiktok"],
                                          you_tube=date["you_tube"])
        await call.message.answer_video(video=date["film"], caption=caption)
        await call.message.answer(text=text)
        await state.finish()
    else:
        text = _("There is an error in adding a movie. ❌")
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())


@dp.callback_query_handler(state=AddFilm.confirmation, text="Not_add", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    text = "stopped adding movies 🛑"
    await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
    await state.finish()
