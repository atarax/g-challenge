from sqlalchemy.orm import Session

from app import crud, models
from app.core.config import settings
from app.schemas.store import StoreCreate
from app.tests.utils.utils import random_lower_string


def create_random_store(db: Session) -> models.Store:
    code = random_lower_string()
    store_in = StoreCreate(code=code)
    return crud.store.create(db=db, obj_in=store_in)


def ensure_default_store(db: Session) -> models.Store:
    code = settings.DEFAULT_STORE
    default_store = crud.store.get_by_code(db, code=code)

    if default_store:
        return default_store

    default_store_in = StoreCreate(code=code)
    return crud.store.create(db=db, obj_in=default_store_in)
