from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Store(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
