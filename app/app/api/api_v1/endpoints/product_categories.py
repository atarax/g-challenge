from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ProductCategory])
def read_categories(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
) -> Any:
    """
    Retrieve product-categories.
    """
    categories = crud.product_category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.post("/", response_model=schemas.ProductCategory)
def create_category(
    *, db: Session = Depends(deps.get_db), category_in: schemas.ProductCategoryCreate,
) -> Any:
    """
    Create new product-category.
    """
    try:
        category = crud.product_category.create(db=db, obj_in=category_in)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Category already exists")
    return category


@router.put("/{id}", response_model=schemas.ProductCategory)
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    category_in: schemas.ProductCategoryUpdate,
) -> Any:
    """
    Update a product-category.
    """
    category = crud.product_category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    try:
        category = crud.product_category.update(
            db=db, db_obj=category, obj_in=category_in
        )
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Category already exists")

    return category


@router.get("/{id}", response_model=schemas.ProductCategory)
def read_category(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Get product-category by ID.
    """
    category = crud.product_category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{id}", response_model=schemas.ProductCategory)
def delete_category(*, db: Session = Depends(deps.get_db), id: int,) -> Any:
    """
    Delete a product-category.
    """
    category = crud.product_category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category = crud.product_category.remove(db=db, id=id)
    return category
