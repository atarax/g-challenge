from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.stock_level import StockLevelCreate

from .product import create_random_product
from .store import create_random_store


def create_random_stock_level(
    db: Session,
    *,
    product_id: Optional[int] = None,
    store_id: Optional[int] = None,
    amount: Optional[int] = 10
) -> models.StockLevel:
    if not product_id:
        product = create_random_product(db)
        product_id = product.id
    if not store_id:
        store = create_random_store(db)
        store_id = store.id

    stock_level_in = StockLevelCreate(
        amount=amount, product_id=product_id, store_id=store_id
    )

    return crud.stock_level.create(db=db, obj_in=stock_level_in)
