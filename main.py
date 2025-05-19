import asyncio
import logging
import signal

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message

#из файлов // from files

from help.config_token import token
bot = Bot(token=token)
dp = Dispatcher()

# Включаем логирование // start logging
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /start // handler for command /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("hi")
    
# Запуск процесса поллинга новых апдейтов // Starting the polling process for new updates
async def main():
    await dp.start_polling(bot)

#Запуск // start main.py

if __name__ == "__main__":
    asyncio.run(main())