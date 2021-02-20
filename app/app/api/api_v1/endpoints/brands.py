from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Brand])
def read_brands(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
) -> Any:
    """
    Retrieve brands.
    """
    brands = crud.brand.get_multi(db, skip=skip, limit=limit)
    return brands


@router.post("/", response_model=schemas.Brand)
def create_brand(
    *, db: Session = Depends(deps.get_db), brand_in: schemas.BrandCreate,
) -> Any:
    """
    Create new brand.
    """
    try:
        brand = crud.brand.create(db=db, obj_in=brand_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Brand already exists")

    return brand


@router.put("/{id}", response_model=schemas.Brand)
def update_brand(
    *, db: Session = Depends(deps.get_db), id: int, brand_in: schemas.BrandUpdate,
) -> Any:
    """
    Update a brand.
    """
    brand = crud.brand.get(db=db, id=id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    try:
        brand = crud.brand.update(db=db, db_obj=brand, obj_in=brand_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Brand already exists")

    return brand


@router.get("/{id}", response_model=schemas.Brand)
def read_brand(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Get brand by ID.
    """
    brand = crud.brand.get(db=db, id=id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand


@router.delete("/{id}", response_model=schemas.Brand)
def delete_brand(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Delete a brand.
    """
    brand = crud.brand.get(db=db, id=id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    brand = crud.brand.remove(db=db, id=id)
    return brand
