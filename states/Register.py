from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    language = State()
    confirmation = State()

class RegisterStateAdmin(StatesGroup):
    language = State()
    confirmation = State()