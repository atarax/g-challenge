import random

from sqlalchemy.orm import Session

from app import crud
from app.schemas.stock_level import StockLevelCreate, StockLevelUpdate
from app.tests.utils.product import create_random_product
from app.tests.utils.store import create_random_store


def test_create_stock_level(db: Session) -> None:
    amount = random.randint(0, int(1e6))
    product = create_random_product(db)
    store = create_random_store(db)

    stock_level_in = StockLevelCreate(
        amount=amount, product_id=product.id, store_id=store.id
    )
    stock_level = crud.stock_level.create(db=db, obj_in=stock_level_in)

    assert stock_level.amount == amount


def test_get_stock_level(db: Session) -> None:
    amount = random.randint(0, int(1e6))
    product = create_random_product(db)
    store = create_random_store(db)

    stock_level_in = StockLevelCreate(
        amount=amount, product_id=product.id, store_id=store.id
    )
    stock_level = crud.stock_level.create(db=db, obj_in=stock_level_in)
    stored_stock_level = crud.stock_level.get(db=db, id=stock_level.id)

    assert stored_stock_level
    assert stock_level.id == stored_stock_level.id
    assert stock_level.amount == stored_stock_level.amount


def test_update_stock_level(db: Session) -> None:
    amount = random.randint(0, int(1e6))
    product = create_random_product(db)
    store = create_random_store(db)

    stock_level_in = StockLevelCreate(
        amount=amount, product_id=product.id, store_id=store.id
    )
    stock_level = crud.stock_level.create(db=db, obj_in=stock_level_in)

    amount2 = random.randint(0, int(1e6))
    stock_level_update = StockLevelUpdate(amount=amount2)
    stock_level2 = crud.stock_level.update(
        db=db, db_obj=stock_level, obj_in=stock_level_update
    )

    assert stock_level.id == stock_level2.id
    assert stock_level.amount == stock_level2.amount
    assert stock_level2.amount == amount2


def test_delete_stock_level(db: Session) -> None:
    amount = random.randint(0, int(1e6))
    product = create_random_product(db)
    store = create_random_store(db)

    stock_level_in = StockLevelCreate(
        amount=amount, product_id=product.id, store_id=store.id
    )
    stock_level = crud.stock_level.create(db=db, obj_in=stock_level_in)
    stock_level2 = crud.stock_level.remove(db=db, id=stock_level.id)
    stock_level3 = crud.stock_level.get(db=db, id=stock_level.id)

    assert stock_level3 is None
    assert stock_level2.id == stock_level.id
    assert stock_level2.amount == amount
