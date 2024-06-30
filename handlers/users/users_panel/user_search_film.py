from aiogram import types

from keyboards.inline.channels import channels
from loader import dp, _
from utils.db_commands.film import get_film_code, get_film_link_instagram, get_film_link_tiktok, get_film_link_you_tube
from utils.db_commands.users import get_user_status
from keyboards.default.user import user_main_menu_def
import re

from utils.function.film_type import film_type_hashtag
from utils.misc.subscription import check_subscription


@dp.message_handler(regexp=re.compile("^\\d{3}$"))
async def user_search_film_handler(message: types.Message):
    if await check_subscription(int(message.chat.id)):
        film = await get_film_code(int(message.text))
        film_status = dict(film)["status"]
        user_status = await get_user_status(int(message.chat.id))
        if film:
            if film_status == "Premium" and user_status == "Free":
                text = ("You need to buy our bot premium to watch this movie\npremium price is 10,000 soums\n"
                        "👤Admin @Misteraxi")
                await message.answer(text=text, reply_markup=await user_main_menu_def())
            else:
                film_type = await film_type_hashtag(film["type"])

                caption_template = _(
                    "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
                    "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
                    "🧩Our Chanel: @Zangoriekran_kanali")
                caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                                  date=film['date'], type=film_type, instagram=film["instagram"],
                                                  tiktok=film["tiktok"], you_tube=film["you_tube"])
                await message.answer_video(video=film["film"], caption=caption)
        else:
            text = _("There is no movie with that code ❗️")
            await message.answer(text=text)
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?instagram\.com\/.*$")
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_link_instagram(message.text)
    film_status = dict(film)["status"]
    user_status = await get_user_status(int(message.chat.id))
    if await check_subscription(int(message.chat.id)):
        if film:
            if film_status == "Premium" and user_status == "Free":
                text = ("You need to buy our bot premium to watch this movie\npremium price is 10,000 soums\n"
                        "👤Admin @Misteraxi")
                await message.answer(text=text, reply_markup=await user_main_menu_def())
            else:
                film_type = await film_type_hashtag(film["type"])
                caption_template = _(
                    "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
                    "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
                    "🧩Our Chanel: @Zangoriekran_kanali")
                caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                                  date=film['date'], type=film_type, instagram=film["instagram"],
                                                  tiktok=film["tiktok"], you_tube=film["you_tube"])
                await message.answer_video(video=film["film"], caption=caption)
        else:
            text = _("There is no movie with that link ❗️")
            await message.answer(text=text)
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)


@dp.message_handler(regexp=r"^https:\/\/(vt\.)?tiktok\.com\/.*$")
async def user_search_film_code_handler(message: types.Message):
    if await check_subscription(int(message.chat.id)):
        film = await get_film_link_tiktok(message.text)
        film_status = dict(film)["status"]
        user_status = await get_user_status(int(message.chat.id))
        if film:
            if film_status == "Premium" and user_status == "Free":
                text = ("You need to buy our bot premium to watch this movie\npremium price is 10,000 soums\n"
                        "👤Admin @Misteraxi")
                await message.answer(text=text, reply_markup=await user_main_menu_def())
            else:
                film_type = await film_type_hashtag(film["type"])
                caption_template = _(
                    "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
                    "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
                    "🧩Our Chanel: @Zangoriekran_kanali")
                caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                                  date=film['date'], type=film_type, instagram=film["instagram"],
                                                  tiktok=film["tiktok"], you_tube=film["you_tube"])
                await message.answer_video(video=film["film"], caption=caption)
        else:
            text = _("There is no movie with that link ❗️")
            await message.answer(text=text)
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?(youtube\.com\/|youtu\.be\/).*")
async def user_search_film_code_handler(message: types.Message):
    if await check_subscription(int(message.chat.id)):
        film = await get_film_link_you_tube(message.text)
        film_status = dict(film)["status"]
        user_status = await get_user_status(int(message.chat.id))
        if film:
            if film_status == "Premium" and user_status == "Free":
                text = ("You need to buy our bot premium to watch this movie\npremium price is 10,000 soums\n"
                        "👤Admin @Misteraxi")
                await message.answer(text=text, reply_markup=await user_main_menu_def())
            else:
                film_type = await film_type_hashtag(film["type"])
                caption_template = _(
                    "🎬Name: {name}\n➖➖➖➖➖➖➖➖➖➖\n📀quality: {quality}\n🌍state: {state}\n📅Date: {date}-year\n"
                    "🎞️type: {type}\n💜Instagram: {instagram}\n🖤Tiktok: {tiktok}\n❤️You Tube: {you_tube}\n"
                    "🧩Our Chanel: @Zangoriekran_kanali")
                caption = caption_template.format(name=film['name'], quality=film['quality'], state=film['state'],
                                                  date=film['date'], type=film_type, instagram=film["instagram"],
                                                  tiktok=film["tiktok"], you_tube=film["you_tube"])
                await message.answer_video(video=film["film"], caption=caption)
        else:
            text = _("There is no movie with that link ❗️")
            await message.answer(text=text)
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)
