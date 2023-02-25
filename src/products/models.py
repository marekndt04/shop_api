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
