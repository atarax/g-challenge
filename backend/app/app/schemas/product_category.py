from pydantic import BaseModel


# Shared properties
class ProductCategoryBase(BaseModel):
    name: str


# Properties to receive on store creation
class ProductCategoryCreate(ProductCategoryBase):
    pass


# Properties to receive on item update
class ProductCategoryUpdate(ProductCategoryBase):
    pass


# Properties shared by models stored in DB
class ProductCategoryInDBBase(ProductCategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class ProductCategory(ProductCategoryInDBBase):
    pass


# Properties properties stored in DB
class ProductCategoryInDB(ProductCategoryInDBBase):
    pass
