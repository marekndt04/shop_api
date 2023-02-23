from fastapi import FastAPI
from motor import motor_asyncio

from src.config import app_settings
from src.products.views import router as products_router

app = FastAPI()
app.include_router(products_router)

mongo_client = motor_asyncio.AsyncIOMotorClient(app_settings.MONGODB_URL)
db = mongo_client.fastapi
products_collection = db.get_collection("products_collection")


@app.get("/healthcheck")
def healthcheck():  # type: ignore # Simple view used as uptests in deployments.
    return {}
