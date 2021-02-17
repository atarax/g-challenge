from .crud_brand import brand
from .crud_item import item
from .crud_product import product
from .crud_product_category import product_category
from .crud_store import store
from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
