from pydantic_settings import BaseSettings
from typing import Optional


class PostgresSettings(BaseSettings):
    POSTGRES_URL_1: str
    POSTGRES_DB_1: str
    POSTGRES_USER_1: str
    POSTGRES_PASSWORD_1: str
    POSTGRES_HOST_1: str
    POSTGRES_PORT_1: int = 5432

    POSTGRES_URL_2: str
    POSTGRES_DB_2: str
    POSTGRES_USER_2: str
    POSTGRES_PASSWORD_2: str
    POSTGRES_HOST_2: str
    POSTGRES_PORT_2: int = 5432


class KafkaSettings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str
    KAFKA_TOPIC_ANALYTICS: str
    KAFKA_GROUP_ID: str


class ClickHouseSettings(BaseSettings):
    CLICKHOUSE_URL: str
    CLICKHOUSE_DATABASE: str
    CLICKHOUSE_USER: str
    CLICKHOUSE_PASSWORD: Optional[str] = None


class TelegramSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str


class AuthSettings(BaseSettings):
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


class AppSettings(BaseSettings):
    APP_NAME: str
    DEBUG: bool = False
    ENVIRONMENT: str


class Settings(BaseSettings):
    postgres: PostgresSettings = PostgresSettings()
    kafka: KafkaSettings = KafkaSettings()
    clickhouse: ClickHouseSettings = ClickHouseSettings()
    telegram: TelegramSettings = TelegramSettings()
    auth: AuthSettings = AuthSettings()
    app: AppSettings = AppSettings()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()