import logging

from app import crud
from app.core.config import settings
from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.schemas.brand import BrandCreate
from app.schemas.product import ProductCreate
from app.schemas.product_category import ProductCategoryCreate
from app.schemas.stock_level import StockLevelCreate
from app.schemas.store import StoreCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)

    # if the default-store does not exist, create it and some more
    # sample data
    code = settings.DEFAULT_STORE
    if crud.store.get_by_code(db, code=code):
        return

    # create default-store
    store_in = StoreCreate(code=code)
    default_store = crud.store.create(db=db, obj_in=store_in)
    # create mm-berlin
    store_in = StoreCreate(code="mm-berlin")
    mm_berlin = crud.store.create(db=db, obj_in=store_in)

    # create some funny brands
    brand_in = BrandCreate(name="Cat co.")
    cat_brand = crud.brand.create(db=db, obj_in=brand_in)
    brand_in = BrandCreate(name="Dog inc.")
    dog_brand = crud.brand.create(db=db, obj_in=brand_in)

    # create some funny categories
    category_in = ProductCategoryCreate(name="cat-toys")
    cat_category = crud.product_category.create(db=db, obj_in=category_in)
    category_in = ProductCategoryCreate(name="dog-toys")
    dog_category = crud.product_category.create(db=db, obj_in=category_in)

    # create some funny products
    product_in = ProductCreate(
        name="piece of string", category_id=cat_category.id, brand_id=cat_brand.id
    )
    cat_product_1 = crud.product.create(db=db, obj_in=product_in)
    product_in = ProductCreate(
        name="leaf", category_id=cat_category.id, brand_id=cat_brand.id
    )
    cat_product_2 = crud.product.create(db=db, obj_in=product_in)

    product_in = ProductCreate(
        name="stick", category_id=dog_category.id, brand_id=dog_brand.id
    )
    dog_product_1 = crud.product.create(db=db, obj_in=product_in)
    product_in = ProductCreate(
        name="ball", category_id=dog_category.id, brand_id=dog_brand.id
    )
    dog_product_2 = crud.product.create(db=db, obj_in=product_in)

    # stock the shops with our supply :)
    # first cat-products
    stock_level_in = StockLevelCreate(
        product_id=cat_product_1.id, store_id=default_store.id, amount=10
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)
    stock_level_in = StockLevelCreate(
        product_id=cat_product_2.id, store_id=default_store.id, amount=20
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)

    stock_level_in = StockLevelCreate(
        product_id=cat_product_1.id, store_id=mm_berlin.id, amount=5
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)
    stock_level_in = StockLevelCreate(
        product_id=cat_product_2.id, store_id=mm_berlin.id, amount=8
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)

    # now dog-products
    stock_level_in = StockLevelCreate(
        product_id=dog_product_1.id, store_id=default_store.id, amount=4
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)
    stock_level_in = StockLevelCreate(
        product_id=dog_product_2.id, store_id=default_store.id, amount=23
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)

    stock_level_in = StockLevelCreate(
        product_id=dog_product_1.id, store_id=mm_berlin.id, amount=7
    )
    # unfortunately mm-berlin run out of balls :(
    crud.stock_level.create(db=db, obj_in=stock_level_in)
    stock_level_in = StockLevelCreate(
        product_id=dog_product_2.id, store_id=mm_berlin.id, amount=0
    )
    crud.stock_level.create(db=db, obj_in=stock_level_in)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
