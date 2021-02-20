from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.store import Store
from app.schemas.store import StoreCreate, StoreUpdate


class CRUDStore(CRUDBase[Store, StoreCreate, StoreUpdate]):
    def get_by_code(self, db: Session, code: str) -> Optional[Store]:
        return db.query(self.model).filter(self.model.code == code).first()


store = CRUDStore(Store)
