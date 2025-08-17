from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_USER_ID: int

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()