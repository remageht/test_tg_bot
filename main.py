import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from config import TOKEN
from handlers.commands import start_command, login_command

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.message.register(start_command, Command(commands=['start']))
dp.message.register(login_command, Command(commands=['login']))

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    asyncio.run(main())