from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Store(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
