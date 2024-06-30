from aiogram.dispatcher.filters.state import StatesGroup, State


class AddFilm(StatesGroup):
    film = State()
    name = State()
    language = State()
    quality = State()
    state = State()
    date = State()
    type = State()
    instagram = State()
    tiktok = State()
    you_tube = State()
    status = State()
    confirmation = State()
