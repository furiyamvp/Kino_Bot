from typing import Union

from aiogram import Bot

from loader import dp


async def check_subscription(user_id):
    try:
        follower = await dp.bot.get_chat_member(chat_id='@Zangoriekran_kanali', user_id=user_id)
        subscription = follower.status in ['member', 'administrator']
    except Exception as e:
        print(f"Error checking subscription: {e}")
        subscription = False

    if subscription:
        return True
    else:
        return False
