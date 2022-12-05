from aiogram.dispatcher.filters.state import State, StatesGroup


class NewsStates(StatesGroup):
    title = State()
    content = State()
    image = State()
