from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Dummy product data
products = [
    {"id": "1", "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": "2", "name": "Shoes", "category": "Fashion", "price": 49.99}
]

cart = []
orders = []

@app.get("/")
async def home():
    return JSONResponse(content={"message": "Welcome to CloudMart!"})

@app.get("/api/v1/products")
async def get_products():
    return products

@app.get("/api/v1/cart")
async def get_cart():
    return cart

@app.post("/api/v1/cart/items")
async def add_to_cart(item: dict):
    cart.append(item)
    return {"status": "added"}

@app.post("/api/v1/orders")
async def create_order(order: dict):
    orders.append(order)
    return {"status": "confirmed"}

@app.get("/health")
async def health():
    return {"status": "ok"}
