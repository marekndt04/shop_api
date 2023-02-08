from fastapi import FastAPI
from src.config import app_settings


app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> dict:
    return {}
