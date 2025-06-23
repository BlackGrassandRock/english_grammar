# handler.py
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from states import Game
from utils import game_step

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer("Привет! Начнём игру.")
    await ask_question(msg, state)

async def ask_question(msg: Message, state: FSMContext):
    truth, question, options = game_step()
    await state.update_data(correct_answer=truth)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=opt)] for opt in options],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await msg.answer(f"Как переводится: <b>{question}</b>?", reply_markup=keyboard)
    await state.set_state(Game.waiting_for_answer)

@router.message(Game.waiting_for_answer)
async def handle_answer(msg: Message, state: FSMContext):
    user_data = await state.get_data()
    correct = user_data["correct_answer"]

    if msg.text == correct:
        await msg.answer("✅ Верно!")
    else:
        await msg.answer(f"❌ Неверно. Правильный ответ: <b>{correct}</b>")

    await ask_question(msg, state)
