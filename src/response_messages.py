from typing import Optional

from pydantic import BaseModel

from .products.models import Product


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
