from fastapi import APIRouter
from ..schemas import MessageRequest, MessageResponse
from ..bot.bot import send_message_to_user
import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

router = APIRouter(
    prefix="",
    tags=["main"]
)


@router.get("/")
async def root():
    return {
        "ok": True,
        "msg": "Успешно получено сообщение"
    }


@router.get("/status")
async def status():
    return {
        "ok": True,
        "msg": "Сервис работает"
    }


@router.get("/echo/{message}")
async def echo_message(message: str):
    return {
        "ok": True,
        "msg": f"Эхо: {message}",
        "received_message": message
    }


@router.post("/send-message", response_model=MessageResponse)
async def send_message(request: MessageRequest):
    print(f"Получено сообщение: {request.msg} для роли: {request.role}")

    try:
        asyncio.create_task(send_message_to_user(f"Новое сообщение ({request.role}): {request.msg}"))
    except Exception as e:
        print(f"Ошибка при отправке в Telegram: {e}")

    return MessageResponse(
        status="ok",
        message="Сообщение успешно получено"
    )