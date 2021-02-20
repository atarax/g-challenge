from sqlalchemy.orm import Session

from app import crud
from app.schemas.product import ProductCreate, ProductUpdate
from app.tests.utils.brand import create_random_brand
from app.tests.utils.product_category import create_random_product_category
from app.tests.utils.utils import random_lower_string


def test_create_product(db: Session) -> None:
    name = random_lower_string()
    category = create_random_product_category(db)
    brand = create_random_brand(db)

    product_in = ProductCreate(name=name, category_id=category.id, brand_id=brand.id)
    product = crud.product.create(db=db, obj_in=product_in)

    assert product.name == name


def test_get_product(db: Session) -> None:
    name = random_lower_string()
    category = create_random_product_category(db)
    brand = create_random_brand(db)

    product_in = ProductCreate(name=name, category_id=category.id, brand_id=brand.id)
    product = crud.product.create(db=db, obj_in=product_in)
    stored_product = crud.product.get(db=db, id=product.id)

    assert stored_product
    assert product.id == stored_product.id
    assert product.name == stored_product.name


def test_update_product(db: Session) -> None:
    name = random_lower_string()
    category = create_random_product_category(db)
    brand = create_random_brand(db)

    product_in = ProductCreate(name=name, category_id=category.id, brand_id=brand.id)
    product = crud.product.create(db=db, obj_in=product_in)

    name2 = random_lower_string()
    product_update = ProductUpdate(name=name2)
    product2 = crud.product.update(db=db, db_obj=product, obj_in=product_update)

    assert product.id == product2.id
    assert product.name == product2.name
    assert product2.name == name2


def test_delete_product(db: Session) -> None:
    name = random_lower_string()
    category = create_random_product_category(db)
    brand = create_random_brand(db)

    product_in = ProductCreate(name=name, category_id=category.id, brand_id=brand.id)
    product = crud.product.create(db=db, obj_in=product_in)
    product2 = crud.product.remove(db=db, id=product.id)
    product3 = crud.product.get(db=db, id=product.id)

    assert product3 is None
    assert product2.id == product.id
    assert product2.name == name
