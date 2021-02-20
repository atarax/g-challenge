from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.product import ProductCreate
from app.tests.utils.utils import random_lower_string

from .brand import create_random_brand
from .product_category import create_random_product_category


def create_random_product(
    db: Session, *, category_id: Optional[int] = None, brand_id: Optional[int] = None
) -> models.Product:
    if not category_id:
        category = create_random_product_category(db)
        category_id = category.id
    if not brand_id:
        brand = create_random_brand(db)
        brand_id = brand.id

    name = random_lower_string()
    product_in = ProductCreate(name=name, category_id=category_id, brand_id=brand_id)
    return crud.product.create(db=db, obj_in=product_in)
