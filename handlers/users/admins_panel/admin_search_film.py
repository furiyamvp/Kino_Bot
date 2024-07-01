from aiogram import types

from keyboards.inline.change_film import admin_film_change_def
from loader import dp, _
from mainn.config import ADMINS
from utils.db_commands.film import get_film_code, get_film_link_instagram, get_film_link_tiktok, get_film_link_you_tube
import re


@dp.message_handler(regexp=re.compile("^\\d{3}$"), chat_id=ADMINS)
async def user_search_film_code(message: types.Message):
    film = await get_film_code(int(message.text))
    if film:
        type_template = film["type"]
        type_strip = type_template.strip()
        type_template_fist_latter = type_strip[0]
        type = type_strip.replace(" ", " #").replace(f"{type_template_fist_latter}", f"#{type_template_fist_latter}")

        caption_template = _(
            "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
            "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
            "🧩Our Chanel: @Zangoriekran_kanali")
        caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                          date=film['date'], type=type, instagram=film["instagram"],
                                          tiktok=film["tiktok"], you_tube=film["you_tube"])
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(int(film['id'])))
    else:
        text = _("There is no movie with that link❗️")
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?instagram\.com\/.*$", chat_id=ADMINS)
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_link_instagram(message.text)
    if film:
        type_template = film["type"]
        type_strip = type_template.strip()
        type_template_fist_latter = type_strip[0]
        type = type_strip.replace(" ", " #").replace(f"{type_template_fist_latter}", f"#{type_template_fist_latter}")

        caption_template = _(
            "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
            "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
            "🧩Our Chanel: @Zangoriekran_kanali")
        caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                          date=film['date'], type=type, instagram=film["instagram"],
                                          tiktok=film["tiktok"], you_tube=film["you_tube"])
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = _("There is no movie with that link❗️")
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(vt\.)?tiktok\.com\/.*$", chat_id=ADMINS)
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_link_tiktok(message.text)
    if film:
        type_template = film["type"]
        type_strip = type_template.strip()
        type_template_fist_latter = type_strip[0]
        type = type_strip.replace(" ", " #").replace(f"{type_template_fist_latter}", f"#{type_template_fist_latter}")

        caption_template = _(
            "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
            "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
            "🧩Our Chanel: @Zangoriekran_kanali")
        caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                          date=film['date'], type=type, instagram=film["instagram"],
                                          tiktok=film["tiktok"], you_tube=film["you_tube"])
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = _("There is no movie with that link ❗️")
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?(youtube\.com\/|youtu\.be\/).*", chat_id=ADMINS)
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_link_you_tube(message.text)
    if film:
        type_template = film["type"]
        type_strip = type_template.strip()
        type_template_fist_latter = type_strip[0]
        type = type_strip.replace(" ", " #").replace(f"{type_template_fist_latter}", f"#{type_template_fist_latter}")

        caption_template = _(
            "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
            "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
            "🧩Our Chanel: @Zangoriekran_kanali")
        caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                          date=film['date'], type=type, instagram=film["instagram"],
                                          tiktok=film["tiktok"], you_tube=film["you_tube"])
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = _("There is no movie with that link ❗️")
        await message.answer(text=text)
