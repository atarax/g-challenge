from sqlalchemy.orm import Session

from app import crud
from app.schemas.store import StoreCreate, StoreUpdate
from app.tests.utils.utils import random_lower_string


def test_create_store(db: Session) -> None:
    code = random_lower_string()
    store_in = StoreCreate(code=code)
    store = crud.store.create(db=db, obj_in=store_in)
    assert store.code == code


def test_get_store(db: Session) -> None:
    code = random_lower_string()
    store_in = StoreCreate(code=code)
    store = crud.store.create(db=db, obj_in=store_in)
    stored_store = crud.store.get(db=db, id=store.id)
    assert stored_store
    assert store.id == stored_store.id
    assert store.code == stored_store.code


def test_update_store(db: Session) -> None:
    code = random_lower_string()
    store_in = StoreCreate(code=code)
    store = crud.store.create(db=db, obj_in=store_in)
    code2 = random_lower_string()
    store_update = StoreUpdate(code=code2)
    store2 = crud.store.update(db=db, db_obj=store, obj_in=store_update)
    assert store.id == store2.id
    assert store.code == store2.code
    assert store2.code == code2


def test_delete_store(db: Session) -> None:
    code = random_lower_string()
    store_in = StoreCreate(code=code)
    store = crud.store.create(db=db, obj_in=store_in)
    store2 = crud.store.remove(db=db, id=store.id)
    store3 = crud.store.get(db=db, id=store.id)
    assert store3 is None
    assert store2.id == store.id
    assert store2.code == code
