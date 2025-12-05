from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: str
    name: str
    category: str
    price: float

class CartItem(BaseModel):
    id: str
    user_id: str
    product_id: str
    quantity: int

class Order(BaseModel):
    id: str
    user_id: str
    items: List[CartItem]
    status: str
