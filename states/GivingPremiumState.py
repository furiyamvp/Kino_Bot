from aiogram.dispatcher.filters.state import StatesGroup, State


class GivingPremium(StatesGroup):
    user_id = State()
    status = State()
