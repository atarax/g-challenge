from typing import Optional

from pydantic import BaseModel

from .brand import Brand
from .product_category import ProductCategory


# Shared properties
class ProductBase(BaseModel):
    name: str


# Properties to receive via API on creation
class ProductCreate(ProductBase):
    brand_id: int
    category_id: int


# Properties to receive via API on update
class ProductUpdate(ProductBase):
    brand_id: Optional[int] = None
    category_id: Optional[int] = None


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Product(ProductInDBBase):
    brand: Brand
    category: ProductCategory


# Additional properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
