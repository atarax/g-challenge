from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .brand import Brand  # noqa: F401
    from .product_category import ProductCategory  # noqa: F401


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand_id = Column(Integer, ForeignKey("brand.id"))
    brand = relationship(
        "Brand", uselist=False, back_populates="products", lazy="subquery"
    )
    category_id = Column(Integer, ForeignKey("product_category.id"))
    category = relationship(
        "ProductCategory", uselist=False, back_populates="products", lazy="subquery"
    )
