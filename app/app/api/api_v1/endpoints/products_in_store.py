from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.ProductInStore])
def get_available_products(
    db: Session = Depends(deps.get_db),
    store_code: str = settings.DEFAULT_STORE,
    only_available: bool = True,
) -> Any:
    """
    Retrieve products.
    """
    store = crud.store.get_by_code(db=db, code=store_code)
    if not store:
        raise HTTPException(
            status_code=404, detail=f"Store with code: {store_code}  not found"
        )

    stock_levels = crud.stock_level.get_multi_by_store_and_availability(
        db, store_id=store.id, only_available=only_available
    )

    result = []
    for stock_level in stock_levels:
        result.append(
            {
                "name": stock_level.product.name,
                "brand": stock_level.product.brand.name,
                "category": stock_level.product.category.name,
                "available": stock_level.amount > 0,
                "amount": stock_level.amount,
            }
        )

    return result
