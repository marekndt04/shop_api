from pydantic import BaseSettings


class AppSettings(BaseSettings):
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str

    class Config:
        env_file = ".env"


app_settings = AppSettings()
