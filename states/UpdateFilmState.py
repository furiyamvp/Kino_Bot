from aiogram.dispatcher.filters.state import StatesGroup, State


class UpdateFilm(StatesGroup):
    film = State()
    name = State()
    state = State()
    date = State()
    type = State()
    instagram = State()
    tiktok = State()
    you_tube = State()
    status = State()
