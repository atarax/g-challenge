from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Store])
def read_stores(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve stores.
    """
    stores = crud.store.get_multi(db, skip=skip, limit=limit)
    return stores

@router.post("/", response_model=schemas.Store)
def create_store(
    *,
    db: Session = Depends(deps.get_db),
    store_in: schemas.StoreCreate,
) -> Any:
    """
    Create new store.
    """
    store = crud.store.create(db=db, obj_in=store_in)
    return store

@router.put("/{id}", response_model=schemas.Store)
def update_store(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    store_in: schemas.StoreUpdate,
) -> Any:
    """
    Update a store.
    """
    store = crud.store.get(db=db, id=id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    store = crud.store.update(db=db, db_obj=store, obj_in=store_in)
    return store

@router.get("/{id}", response_model=schemas.Store)
def read_store(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get store by ID.
    """
    store = crud.store.get(db=db, id=id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.delete("/{id}", response_model=schemas.Store)
def delete_store(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a store.
    """
    store = crud.store.get(db=db, id=id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    store = crud.store.remove(db=db, id=id)
    return store

