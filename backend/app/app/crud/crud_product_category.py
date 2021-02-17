from app.crud.base import CRUDBase
from app.models.product_category import ProductCategory
from app.schemas.product_category import ProductCategoryCreate, ProductCategoryUpdate


class CRUDStore(
    CRUDBase[ProductCategory, ProductCategoryCreate, ProductCategoryUpdate]
):
    pass


product_category = CRUDStore(ProductCategory)
