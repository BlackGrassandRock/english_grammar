# states.py
from aiogram.fsm.state import State, StatesGroup

class Game(StatesGroup):
    waiting_for_answer = State()
