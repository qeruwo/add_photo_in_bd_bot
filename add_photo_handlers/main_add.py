import asyncio, os

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery, FSInputFile

from keyboards.main_keyboard import add_photo_keyboard
from help.texts import add_main_catalog
from help.config import all_media_dir

rt = Router()

class add_photo(StatesGroup):
    photo_give = State()
    text_give = State()
    give_results = State()

@rt.callback_query(F.data == "add_photo", StateFilter(None))
async def open_add_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text=add_main_catalog, reply_markup=add_photo_keyboard)
    await call.answer()
    await state.set_state(add_photo.photo_give)
    
@rt.message(add_photo.photo_give)
async def add_photo_in_bd(message: Message, state: FSMContext):
    if message.photo:
        file_name = f"photos/{message.photo[-1].file_id}.jpg"
        await message.answer(file_name)
        await message.bot.download(message.photo[-1], destination=file_name)
        photo = FSInputFile(path=file_name, filename=file_name)
        await message.answer_photo(photo=photo, caption="ssss")
    else:
        await message.answer("Ничего нет или вы сжали изображение.")
