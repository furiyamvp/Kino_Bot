from aiogram import types
from keyboards.default.back import main_menu_back
from keyboards.inline.channels import channels
from loader import dp, _
from utils.misc.subscription import check_subscription


@dp.message_handler(text=["Call-markaz 📞", "Колл-центр 📞", "Call-markaz 📞"], state="*")
async def call_center_handler(message: types.Message):
    if await check_subscription(int(message.chat.id)):
        text = """
1) @furiya_yunus
2) @Misteraxi
"""
        await message.answer(text=text, reply_markup=await main_menu_back())
    else:
        await message.reply(
            _("You have not subscribed to the channels!\n"
              "After subscribing, press /start to activate the bot."),
            reply_markup=channels)