from aiogram import Bot, html, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart

import sys
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

token = os.environ.get("TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def welcome(message: Message):
    print(f"the user: {message.from_user.full_name} just started the bot")
    await message.answer(f'hi {html.bold(message.from_user.full_name)}')

async def main():
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    