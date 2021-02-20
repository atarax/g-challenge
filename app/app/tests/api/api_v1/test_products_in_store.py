from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.product import create_random_product
from app.tests.utils.stock_level import create_random_stock_level
from app.tests.utils.store import create_random_store, ensure_default_store
from app.tests.utils.utils import random_lower_string


def test_available_product_default_store(client: TestClient, db: Session) -> None:
    default_store = ensure_default_store(db)
    product = create_random_product(db)
    amount = 1
    create_random_stock_level(
        db, product_id=product.id, store_id=default_store.id, amount=amount
    )

    response = client.get(f"{settings.API_V1_STR}/products_in_store",)
    assert response.status_code == 200

    content = response.json()
    all_available = True
    product_found = None

    # check if only available items are returned, available is correctly set
    # and the product we just added is contained
    for result in content:
        all_available = all_available & (result["amount"] > 0) & result["available"]
        if (
            result["name"] == product.name
            and result["amount"] == amount
            and result["category"] == product.category.name
            and result["brand"] == product.brand.name
        ):
            product_found = True

    assert all_available
    assert product_found


def test_non_available_product_default_store(client: TestClient, db: Session) -> None:
    default_store = ensure_default_store(db)
    product = create_random_product(db)
    amount = 0
    create_random_stock_level(
        db, product_id=product.id, store_id=default_store.id, amount=amount
    )

    response = client.get(
        f"{settings.API_V1_STR}/products_in_store?only_available=false",
    )
    assert response.status_code == 200

    content = response.json()
    product_found = False

    # check if the product with zero amount we just created is contained
    for result in content:
        if (
            result["name"] == product.name
            and result["amount"] == amount
            and result["category"] == product.category.name
            and result["brand"] == product.brand.name
        ):
            product_found = True

    assert product_found


def test_non_default_store(client: TestClient, db: Session) -> None:
    store = create_random_store(db)
    product = create_random_product(db)
    non_available_product = create_random_product(db)
    amount = 1
    create_random_stock_level(
        db, product_id=product.id, store_id=store.id, amount=amount
    )
    create_random_stock_level(
        db, product_id=non_available_product.id, store_id=store.id, amount=0
    )

    response = client.get(
        f"{settings.API_V1_STR}/products_in_store?store_code={store.code}",
    )
    assert response.status_code == 200

    # result should contain only the one product we added for a non-default store
    content = response.json()
    assert len(content) == 1

    if (
        content[0]["name"] == product.name
        and content[0]["amount"] == amount
        and content[0]["category"] == product.category.name
        and content[0]["brand"] == product.brand.name
    ):
        product_found = True

    assert product_found


def test_non_existent_store(client: TestClient, db: Session) -> None:
    non_existent_store_name = random_lower_string()

    response = client.get(
        f"{settings.API_V1_STR}/products_in_store?store_code={non_existent_store_name}",
    )
    assert response.status_code == 404
