from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.brand import BrandCreate
from app.tests.utils.utils import random_lower_string


def create_random_brand(db: Session) -> models.Brand:
    name = random_lower_string()
    brand_in = BrandCreate(name=name)
    return crud.brand.create(db=db, obj_in=brand_in)
