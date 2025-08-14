import asyncio
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from ..config import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

async def send_message_to_user(message_text: str):
    try:
        await bot.send_message(chat_id=settings.TELEGRAM_USER_ID, text=message_text)
        logging.info(f"Сообщение отправлено пользователю {settings.TELEGRAM_USER_ID}")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Это эхо-бот, повторяет сообщения")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Эхо-бот\n"
        "повторяет сообщения.\n"
        "Доступные команды:\n"
        "/start - Начать работу\n"
        "/help - Показать помощь"
    )
    await message.answer(help_text)

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"{message.text}")

async def main():
    logging.info("Бот запускается...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())