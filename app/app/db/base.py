# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.brand import Brand  # noqa
from app.models.product import Product  # noqa
from app.models.product_category import ProductCategory  # noqa
from app.models.store import Store  # noqa
