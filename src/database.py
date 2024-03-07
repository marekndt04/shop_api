from motor import motor_asyncio

from .config import app_settings

mongo_db_url = (
    f"mongodb://{app_settings.MONGO_USERNAME}:{app_settings.MONGO_PASSWORD}"
    f"@{app_settings.MONGO_HOST}:{app_settings.MONGO_PORT}"
)
mongo_client = motor_asyncio.AsyncIOMotorClient(mongo_db_url)  # type: ignore
db = mongo_client[app_settings.MONGO_DATABASE]


# test change to trigger a comment
def setup_collections() -> None:
    products_collection = db["products_collection"]
    # Below line is ingored because mypy throws [coroutine-unused] error, while this
    # function is passed to FastAPI as a argument to startup event handler.
    products_collection.create_index("name", unique=True)  # type: ignore
