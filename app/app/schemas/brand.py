from pydantic import BaseModel


# Shared properties
class BrandBase(BaseModel):
    name: str


# Properties to receive on store creation
class BrandCreate(BrandBase):
    pass


# Properties to receive on item update
class BrandUpdate(BrandBase):
    pass


# Properties shared by models stored in DB
class BrandInDBBase(BrandBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Brand(BrandInDBBase):
    pass


# Properties properties stored in DB
class BrandInDB(BrandInDBBase):
    pass
