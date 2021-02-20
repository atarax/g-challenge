from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.StockLevel])
def read_stock_levels(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
) -> Any:
    """
    Retrieve stock_levels.
    """
    stock_levels = crud.stock_level.get_multi(db, skip=skip, limit=limit)
    return stock_levels


@router.post("/", response_model=schemas.StockLevel)
def create_stock_level(
    *, db: Session = Depends(deps.get_db), stock_level_in: schemas.StockLevelCreate,
) -> Any:
    """
    Create new stock_level.
    """
    try:
        stock_level = crud.stock_level.create(db=db, obj_in=stock_level_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="StockLevel already exists")
    return stock_level


@router.put("/{id}", response_model=schemas.StockLevel)
def update_stock_level(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    stock_level_in: schemas.StockLevelUpdate,
) -> Any:
    """
    Update an stock_level.
    """
    stock_level = crud.stock_level.get(db=db, id=id)
    if not stock_level:
        raise HTTPException(status_code=404, detail="StockLevel not found")

    try:
        stock_level = crud.stock_level.update(
            db=db, db_obj=stock_level, obj_in=stock_level_in
        )
    except IntegrityError:
        raise HTTPException(status_code=400, detail="StockLevel already exists")

    return stock_level


@router.get("/{id}", response_model=schemas.StockLevel)
def read_stock_level(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Get stock_level by ID.
    """
    stock_level = crud.stock_level.get(db=db, id=id)
    if not stock_level:
        raise HTTPException(status_code=404, detail="StockLevel not found")
    return stock_level


@router.delete("/{id}", response_model=schemas.StockLevel)
def delete_stock_level(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Delete an stock_level.
    """
    stock_level = crud.stock_level.get(db=db, id=id)
    if not stock_level:
        raise HTTPException(status_code=404, detail="StockLevel not found")
    stock_level = crud.stock_level.remove(db=db, id=id)
    return stock_level
