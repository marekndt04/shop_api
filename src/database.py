from motor import motor_asyncio

from .config import app_settings

mongo_client = motor_asyncio.AsyncIOMotorClient(app_settings.MONGODB_URL)
db = mongo_client.fastapi
