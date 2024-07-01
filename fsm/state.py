from aiogram.fsm.state import State, StatesGroup


class FSMregistaration(StatesGroup):
    FIO = State()
    photo = State()
    location = State()
