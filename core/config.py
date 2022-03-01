from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")

    CORS_ORIGINS = [
        "http://localhost",
        "http://localhost:3000",
    ]

settings: Settings = Settings()