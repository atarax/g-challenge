from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    brands,
    product_categories,
    products,
    products_in_store,
    stock_levels,
    stores,
)

api_router = APIRouter()

api_router.include_router(
    products_in_store.router, prefix="/products_in_store", tags=["products_in_store"]
)
api_router.include_router(
    stock_levels.router, prefix="/stock_levels", tags=["stock_levels"]
)
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(brands.router, prefix="/brands", tags=["brands"])
api_router.include_router(stores.router, prefix="/stores", tags=["stores"])
api_router.include_router(
    product_categories.router, prefix="/product_categories", tags=["product_categories"]
)
