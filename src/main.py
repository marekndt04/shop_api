from fastapi import FastAPI

from src.products.views import router as products_router

app = FastAPI()
app.include_router(products_router)


@app.get("/healthcheck")
def healthcheck():  # type: ignore # Simple view used as uptests in deployments.
    return {}
