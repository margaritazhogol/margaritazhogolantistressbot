
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)
from dotenv import load_dotenv

import database
from questions import (
    ANSWER_OPTIONS,
    ANSWER_WEIGHTS,
    DISCLAIMER_TEXT,
    QUESTIONS,
    SOS_BUTTON_TEXT,
    SOS_TEXT,
    get_result_for_score,
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
PROXY_URL = os.getenv("PROXY_URL")

logging.basicConfig(level=logging.INFO)
router = Router()


class QuizStates(StatesGroup):
    answering = State()


def get_persistent_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=SOS_BUTTON_TEXT)]],
        resize_keyboard=True,
        is_persistent=True,
    )


def get_question_keyboard(question_index: int) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=option, callback_data=f"answer:{question_index}:{option}")]
        for option in ANSWER_OPTIONS
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def send_question(message: Message, question_index: int) -> None:
    question_text = QUESTIONS[question_index]
    await message.answer(
        f"Вопрос {question_index + 1}/{len(QUESTIONS)}\n\n{question_text}",
        reply_markup=get_question_keyboard(question_index),
    )


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(DISCLAIMER_TEXT, reply_markup=get_persistent_keyboard())
    await state.set_state(QuizStates.answering)
    await state.update_data(score=0, question_index=0)
    await send_question(message, question_index=0)


@router.message(F.text == SOS_BUTTON_TEXT)
async def sos_handler(message: Message) -> None:
    await message.answer(SOS_TEXT)


@router.callback_query(F.data.startswith("answer:"))
async def handle_answer(callback, state: FSMContext) -> None:
    _, question_index_str, answer_option = callback.data.split(":", 2)
    question_index = int(question_index_str)

    data = await state.get_data()
    if data.get("question_index") != question_index:
        await callback.answer("Этот вопрос уже отвечен")
        return

    score = data.get("score", 0) + ANSWER_WEIGHTS[answer_option]
    next_index = question_index + 1

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer()

    if next_index < len(QUESTIONS):
        await state.update_data(score=score, question_index=next_index)
        await send_question(callback.message, next_index)
    else:
        await finish_quiz(callback.message, state, score)


async def finish_quiz(message: Message, state: FSMContext, score: int) -> None:
    result = get_result_for_score(score)
    await message.answer(
        f"Тест завершён! Твой результат: {score} из 60 баллов.\n\n"
        f"{result['title']}\n\n{result['text']}"
    )

    user = message.chat
    database.save_result(
        user_id=user.id,
        username=user.username,
        score=score,
        result_title=result["title"],
    )
    await state.clear()


async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("Не найден BOT_TOKEN в .env")

    database.init_db()

    session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else None
    bot = Bot(token=BOT_TOKEN, session=session)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
