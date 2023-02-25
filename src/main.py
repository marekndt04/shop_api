from fastapi import FastAPI

from src.database import setup_collections
from src.products.views import router as products_router

app = FastAPI()
app.add_event_handler("startup", setup_collections)

app.include_router(products_router)


@app.get("/healthcheck")
def healthcheck():  # type: ignore # Simple view used as uptests in deployments.
    return {}
