from fastapi import FastAPI
from src.schemas import MessageRequest, MessageResponse
from src.bot.bot import send_message_to_user
import asyncio

app = FastAPI(
    title="FastAPI App",
    description="FastAPI application for message processing"
)


@app.get("/")
async def root():
    return {
        "ok": True,
        "msg": "Успешно получено сообщение"
    }


@app.get("/status")
async def status():
    return {
        "ok": True,
        "msg": "Сервис работает"
    }


@app.get("/echo/{message}")
async def echo_message(message: str):
    return {
        "ok": True,
        "msg": f"Эхо: {message}",
        "received_message": message
    }


@app.post("/send-message", response_model=MessageResponse)
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.app:app", host="127.0.0.1", port=8000, reload=True)