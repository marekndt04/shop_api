from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/products")
async def get_products() -> Dict:
    return {}
