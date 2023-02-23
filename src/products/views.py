from typing import List

from fastapi import APIRouter

from src.products.models import Product

from ..database import db

router = APIRouter()

products_collection = db.get_collection("products_collection")


@router.get("/products")
async def get_products() -> List[Product]:
    products = []
    async for product in products_collection.find():
        products.append(Product(**product))
    return products
