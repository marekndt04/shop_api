from motor import motor_asyncio

from .config import app_settings

mongo_client = motor_asyncio.AsyncIOMotorClient(app_settings.MONGODB_URL)
db = mongo_client.fastapi
db.create_collection("products_collection")

products_collection = db.get_collection("products_collection")
products_collection.create_index("name", unique=True)
