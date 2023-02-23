from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "description": "Some description",
                "price": 10.0,
                "quantity": "666",
            }
        }
