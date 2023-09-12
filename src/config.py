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

    class Config:
        env_file = ".env"


app_settings = AppSettings()
