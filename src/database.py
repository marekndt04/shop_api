from motor import motor_asyncio

from .config import app_settings

mongo_db_url = (
    f"mongodb://{app_settings.MONGO_USERNAME}:{app_settings.MONGO_PASSWORD}"
    f"@{app_settings.MONGO_HOST}:{app_settings.MONGO_PORT}"
)
mongo_client = motor_asyncio.AsyncIOMotorClient(mongo_db_url)
db = mongo_client[app_settings.MONGO_DATABASE]


def setup_collections() -> None:
    products_collection = db["products_collection"]
    products_collection.create_index("name", unique=True)
