from sqlalchemy.orm import Session

from app import crud
from app.schemas.product_category import ProductCategoryCreate, ProductCategoryUpdate
from app.tests.utils.utils import random_lower_string


def test_create_product_category(db: Session) -> None:
    name = random_lower_string()
    category_in = ProductCategoryCreate(name=name)
    category = crud.product_category.create(db=db, obj_in=category_in)
    assert category.name == name


def test_get_product_category(db: Session) -> None:
    name = random_lower_string()
    category_in = ProductCategoryCreate(name=name)
    category = crud.product_category.create(db=db, obj_in=category_in)
    stored_category = crud.product_category.get(db=db, id=category.id)
    assert stored_category
    assert category.id == stored_category.id
    assert category.name == stored_category.name


def test_update_product_category(db: Session) -> None:
    name = random_lower_string()
    category_in = ProductCategoryCreate(name=name)
    category = crud.product_category.create(db=db, obj_in=category_in)
    name2 = random_lower_string()
    category_update = ProductCategoryUpdate(name=name2)
    category2 = crud.product_category.update(
        db=db, db_obj=category, obj_in=category_update
    )
    assert category.id == category2.id
    assert category.name == category2.name
    assert category2.name == name2


def test_delete_product_category(db: Session) -> None:
    name = random_lower_string()
    category_in = ProductCategoryCreate(name=name)
    category = crud.product_category.create(db=db, obj_in=category_in)
    category2 = crud.product_category.remove(db=db, id=category.id)
    category3 = crud.product_category.get(db=db, id=category.id)
    assert category3 is None
    assert category2.id == category.id
    assert category2.name == name
