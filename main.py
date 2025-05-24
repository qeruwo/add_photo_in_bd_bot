import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message

#из файлов // from files
from help.config_token import token
from keyboards.main_keyboard import keyboard
from help.texts import main_text
from add_photo_handlers import main_add

bot = Bot(token=token)
dp = Dispatcher()

# Включаем логирование // start logging
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /start // handler for command /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text=main_text, reply_markup=keyboard)
    
# Запуск процесса поллинга новых апдейтов // Starting the polling process for new updates
async def main():
    dp.include_router(main_add.rt)
    await dp.start_polling(bot)
#Запуск // start main.py
if __name__ == "__main__":
    asyncio.run(main())