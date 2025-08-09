from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title = "FastAPI App",
    description = "FastAPI приложение"
)


@app.get("/")
async def root():
    return {
        "ok": True,
        "msg": "Success receive message"
    }

@app.get("/status")
async def status():
    return {
        "ok": True,
        "msg": "Service is running"
    }

@app.get("/echo/{message}")
async def echo_message(message: str):
    return {
        "ok": True,
        "msg": f"Echo: {message}",
        "received_message": message
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)