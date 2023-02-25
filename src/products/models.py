from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        schema_extra = {
            "example": {
                "name": "New product",
                "description": "Some description",
                "price": 10.0,
                "quantity": "666",
            }
        }


class HttpCreatedBody(BaseModel):
    message: Optional[str] = "Created"
    body: Product

    class Config:
        schema_extra = {
            "example": {
                "message": "OK",
                "body": Product.schema()["example"],
            }
        }


class HttpConflictBody(BaseModel):
    message: Optional[str] = "Duplicated"
    body: str
