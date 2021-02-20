from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401
    from .store import Store  # noqa: F401


class StockLevel(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", uselist=False, lazy="subquery")
    store_id = Column(Integer, ForeignKey("store.id"))
    store = relationship("Store", uselist=False, lazy="subquery")
    amount = Column(Integer, index=False, nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        return "stock_level"
