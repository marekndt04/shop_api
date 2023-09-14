import os

from pydantic import validator
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str
    MONGO_PORT: int
    MONGO_HOST: str = "localhost"

    @validator("MONGO_PORT", pre=True)
    def cast_port(cls, v):
        return int(v)


mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_database = os.getenv("MONGO_DATABASE")
mongo_port = os.getenv("MONGO_PORT")
mongo_host = os.getenv("MONGO_HOST", "localhost")


app_settings = AppSettings(
    MONGO_USERNAME=mongo_username,
    MONGO_PASSWORD=mongo_password,
    MONGO_DATABASE=mongo_database,
    MONGO_PORT=mongo_port,
    MONGO_HOST=mongo_host,
)
