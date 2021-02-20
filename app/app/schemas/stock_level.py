from typing import Optional

from pydantic import BaseModel

from .product import Product
from .store import Store


# Shared properties
class StockLevelBase(BaseModel):
    amount: int


# Properties to receive via API on creation
class StockLevelCreate(StockLevelBase):
    product_id: int
    store_id: int


# Properties to receive via API on update
class StockLevelUpdate(StockLevelBase):
    product_id: Optional[int] = None
    store_id: Optional[int] = None


# Properties shared by models stored in DB
class StockLevelInDBBase(StockLevelBase):
    id: int
    amount: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class StockLevel(StockLevelInDBBase):
    product: Product
    store: Store
    amount: int


# Additional properties stored in DB
class StockLevelInDB(StockLevelInDBBase):
    pass
