import http
from typing import List

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from ..database import db
from ..response_messages import HttpConflictBody, HttpCreatedBody
from .models import Product

router = APIRouter()
products_collection = db["products_collection"]


@router.get("/products/")
async def get_products() -> List[Product]:
    products = []
    async for product in products_collection.find():
        products.append(Product(**product))
    return products


@router.post("/products/")
async def create_products(product: Product) -> Response:
    product_dict = product.model_dump()

    try:
        await products_collection.insert_one(product_dict)
    except DuplicateKeyError:
        status_code = http.HTTPStatus.CONFLICT
        description = f"product with name '{product_dict['name']}' already exists"
        content = HttpConflictBody(body=description).model_dump()
    else:
        status_code = http.HTTPStatus.CREATED
        content = HttpCreatedBody(body=product_dict).model_dump()

    return JSONResponse(status_code=status_code, content=content)
