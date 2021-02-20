from sqlalchemy.orm import Session

from app import crud
from app.schemas.brand import BrandCreate, BrandUpdate
from app.tests.utils.utils import random_lower_string


def test_create_brand(db: Session) -> None:
    name = random_lower_string()
    brand_in = BrandCreate(name=name)
    brand = crud.brand.create(db=db, obj_in=brand_in)
    assert brand.name == name


def test_get_brand(db: Session) -> None:
    name = random_lower_string()
    brand_in = BrandCreate(name=name)
    brand = crud.brand.create(db=db, obj_in=brand_in)
    stored_brand = crud.brand.get(db=db, id=brand.id)
    assert stored_brand
    assert brand.id == stored_brand.id
    assert brand.name == stored_brand.name


def test_update_brand(db: Session) -> None:
    name = random_lower_string()
    brand_in = BrandCreate(name=name)
    brand = crud.brand.create(db=db, obj_in=brand_in)
    name2 = random_lower_string()
    brand_update = BrandUpdate(name=name2)
    brand2 = crud.brand.update(db=db, db_obj=brand, obj_in=brand_update)
    assert brand.id == brand2.id
    assert brand.name == brand2.name
    assert brand2.name == name2


def test_delete_brand(db: Session) -> None:
    name = random_lower_string()
    brand_in = BrandCreate(name=name)
    brand = crud.brand.create(db=db, obj_in=brand_in)
    brand2 = crud.brand.remove(db=db, id=brand.id)
    brand3 = crud.brand.get(db=db, id=brand.id)
    assert brand3 is None
    assert brand2.id == brand.id
    assert brand2.name == name
