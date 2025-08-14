import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from fastapi import FastAPI
from src.api.router import router

app = FastAPI(
    title="FastAPI App",
    description="FastAPI application for message processing"
)

app.include_router(router)