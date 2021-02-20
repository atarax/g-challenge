from pydantic import BaseModel


# Shared properties
class ProductInStore(BaseModel):
    name: str
    brand: str
    category: str
    available: bool
    amount: int
