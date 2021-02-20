from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401


class ProductCategory(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    products = relationship("Product", back_populates="category")

    @declared_attr
    def __tablename__(cls) -> str:
        return "product_category"
