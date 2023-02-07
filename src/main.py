from fastapi import FastAPI
from src.config import app_settings

app = FastAPI()

@app.get("/healthcheck")
def read_root():
    return {"asd": app_settings.MONGO_DATABASE}
