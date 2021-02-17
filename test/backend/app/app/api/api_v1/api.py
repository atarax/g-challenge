from fastapi import APIRouter

from app.api.api_v1.endpoints import (
  items, 
  login, 
  users, 
  stores,
  product_categories
)

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(stores.router, prefix="/stores", tags=["stores"])
api_router.include_router(product_categories.router, prefix="/product_categories", tags=["product_categories"])
