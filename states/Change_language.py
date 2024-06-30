from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeLanguage(StatesGroup):
    language = State()
