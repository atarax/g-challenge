from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.product_category import ProductCategoryCreate
from app.tests.utils.utils import random_lower_string


def create_random_product_category(db: Session) -> models.ProductCategory:
    name = random_lower_string()
    category_in = ProductCategoryCreate(name=name)
    return crud.product_category.create(db=db, obj_in=category_in)
