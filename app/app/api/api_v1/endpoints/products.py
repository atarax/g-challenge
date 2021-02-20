from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Product])
def read_products(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
) -> Any:
    """
    Retrieve products.
    """
    products = crud.product.get_multi(db, skip=skip, limit=limit)
    return products


@router.post("/", response_model=schemas.Product)
def create_product(
    *, db: Session = Depends(deps.get_db), product_in: schemas.ProductCreate,
) -> Any:
    """
    Create new product.
    """
    try:
        product = crud.product.create(db=db, obj_in=product_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Product already exists")
    return product


@router.put("/{id}", response_model=schemas.Product)
def update_product(
    *, db: Session = Depends(deps.get_db), id: int, product_in: schemas.ProductUpdate,
) -> Any:
    """
    Update an product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    try:
        product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Product already exists")

    return product


@router.get("/{id}", response_model=schemas.Product)
def read_product(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Get product by ID.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{id}", response_model=schemas.Product)
def delete_product(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Delete an product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.product.remove(db=db, id=id)
    return product
