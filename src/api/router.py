from fastapi import APIRouter
from src.schemas.schemas import MessageRequest, MessageResponse
from ..bot.bot import send_message_to_user
import asyncio
import sys
import os
from src.celery_app import celery_app
from src.tasks import send_telegram_message_async, add_numbers


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

@router.post("/send-message-async")
async def send_message_async(request: MessageRequest):
    print(f"Поставлена в очередь задача: {request.msg} для роли: {request.role}")
    task = send_telegram_message_async.delay(f"Новое сообщение ({request.role}): {request.msg}")

    return MessageResponse(
        status="ok",
        message=f"Сообщение поставлено в очередь. ID задачи: {task.id}"
    )

@router.post("/add-task")
async def add_task_endpoint(x: int, y: int):
    task = add_numbers.delay(x, y)
    return {
        "status": "ok",
        "message": "Задача сложения поставлена в очередь",
        "task_id": task.id
    }

@router.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status, # PENDING, STARTED, SUCCESS, FAILURE, ...
        "result": task_result.result if task_result.ready() else None
    }
