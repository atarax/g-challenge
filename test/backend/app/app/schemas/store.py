from typing import Optional

from pydantic import BaseModel


# Shared properties
class StoreBase(BaseModel):
    code: str

# Properties to receive on store creation
class StoreCreate(StoreBase):
    pass


# Properties to receive on item update
class StoreUpdate(ItemBase):
    pass


# Properties shared by models stored in DB
class StoreInDBBase(StoreBase):
    id: int
    code: str

    class Config:
        orm_mode = True


# Properties to return to client
class Store(StoreInDBBase):
    pass


# Properties properties stored in DB
class StoreInDB(StoreInDBBase):
    pass
