from motor import motor_asyncio

from .config import app_settings

mongo_client = motor_asyncio.AsyncIOMotorClient(app_settings.MONGODB_URL)
db = mongo_client[app_settings.MONGO_DATABASE]


def setup_collections() -> None:
    products_collection = db["products_collection"]
    products_collection.create_index("name", unique=True)
