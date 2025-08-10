from fastapi import FastAPI
from schemas import MessageRequest, MessageResponse
import uvicorn

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

    return MessageResponse(
        status="ok",
        message="Сообщение успешно получено"
    )


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)