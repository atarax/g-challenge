from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class ProductCategory(Base):
    __tablename__ = "product_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
