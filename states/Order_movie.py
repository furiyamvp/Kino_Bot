from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderMovie(StatesGroup):
    text = State()
