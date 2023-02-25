import http
from typing import List

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from src.products.models import HttpCreatedBody, Product

from ..database import db

router = APIRouter()

products_collection = db.get_collection("products_collection")


@router.get("/products/")
async def get_products() -> List[Product]:
    products = []
    async for product in products_collection.find():
        products.append(Product(**product))
    return products


@router.post("/products/")
async def create_products(product: Product) -> Response:
    product_dict = product.dict()
    await products_collection.insert_one(product.dict())
    return JSONResponse(
        status_code=http.HTTPStatus.CREATED,
        content=HttpCreatedBody(body=product_dict).dict(),
    )
