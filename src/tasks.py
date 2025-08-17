from src.celery_app import celery_app
import time
from src.config import settings
import asyncio
from aiogram import Bot

@celery_app.task
def send_telegram_message_async(message_text: str):
    try:
        asyncio.run(_send_message(message_text))
        return f"Сообщение '{message_text}' отправлено успешно"
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
        raise

async def _send_message(message_text: str):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    try:
        await bot.send_message(chat_id=settings.TELEGRAM_USER_ID, text=message_text)
    finally:
        await bot.session.close()

@celery_app.task
def add_numbers(x:int, y: int) -> int:
    time.sleep(5)
    result = x + y
    print(f"Результат сложения {x} + {y} = {result}")
    return result