# database implementation
from sqlmodel import SQLModel, Session, create_engine, select, Field

# models
class Song(SQLModel, table= True):
    song_id : int = Field(primary_key=True)
    coverart : str |  None = None
    song_no : str | None = None
    name : str = Field(index=True)
    artist: str = Field(index=True)
    duration: str
    download_link : str

engine = create_engine("sqlite:///server.db")

def create_data():
    SQLModel.metadata.create_all(engine)

def fetch_data(song: str):
    with Session(engine) as session:
        statement = select(Song).where(Song.name.like(f"%{song}%"))
        results = session.exec(statement)
        data = [i for i in results]
        return data[0]
        # for result in results:
        #     return result.download_link

# bot implementation
from aiogram import Dispatcher, html, Bot
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, URLInputFile

import os
import asyncio



bot_token = os.getenv("TOKEN")
print(bot_token)

dp =  Dispatcher()

@dp.message(CommandStart())
async def welcome(message: Message):
    await message.answer(f"which song are searching for today, {html.bold(message.from_user.full_name)}")

@dp.message()
async def downloder(message: Message):
    song = fetch_data(message.text)
    data =  URLInputFile(
        song.download_link, filename=f"{song.name} - {song.artist}.mp3"
    )
    await Bot.send_audio(self= Bot(token=bot_token), chat_id=message.chat.id, audio=data, caption='🔥')

async def main():
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    create_data()
    asyncio.run(main())