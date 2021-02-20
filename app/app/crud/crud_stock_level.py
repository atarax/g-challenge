from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.stock_level import StockLevel
from app.schemas.stock_level import StockLevelCreate, StockLevelUpdate


class CRUDStockLevel(CRUDBase[StockLevel, StockLevelCreate, StockLevelUpdate]):
    def get_multi_by_store_and_availability(
        self,
        db: Session,
        *,
        store_id: int,
        only_available: bool = True,
        skip: int = 0,
        limit: int = 100
    ) -> List[StockLevel]:

        filter = StockLevel.store_id == store_id
        if only_available:
            filter = filter & (StockLevel.amount > 0)

        return db.query(self.model).filter(filter).offset(skip).limit(limit).all()


stock_level = CRUDStockLevel(StockLevel)
