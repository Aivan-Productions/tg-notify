from fastapi import FastAPI
from src.api.router import router

app = FastAPI(
    title="FastAPI App",
    description="FastAPI application for message processing"
)

app.include_router(router)