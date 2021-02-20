import random

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.tests.utils.product import create_random_product
from app.tests.utils.stock_level import create_random_stock_level
from app.tests.utils.store import create_random_store


def test_read_stock_levels(client: TestClient, db: Session) -> None:
    stock_level = create_random_stock_level(db)
    # this will fail if the test-database is never cleaned up
    limit = int(1e6)
    response = client.get(f"{settings.API_V1_STR}/stock_levels?limit={limit}",)
    assert response.status_code == 200
    content = response.json()

    found_stock_level = None
    for stock_level_in_result in content:
        if stock_level.id == stock_level_in_result["id"]:
            found_stock_level = stock_level_in_result
            break

    assert found_stock_level
    assert found_stock_level["amount"] == stock_level.amount


def test_create_stock_level(client: TestClient, db: Session) -> None:
    amount = random.randint(0, int(1e6))
    product = create_random_product(db)
    store = create_random_store(db)

    data = {"amount": amount, "product_id": product.id, "store_id": store.id}
    response = client.post(f"{settings.API_V1_STR}/stock_levels/", json=data,)

    assert response.status_code == 200
    content = response.json()
    assert content["amount"] == data["amount"]
    assert "id" in content


def test_fail_on_create_duplicate_stock_level(client: TestClient, db: Session) -> None:
    stock_level = create_random_stock_level(db)
    product = stock_level.product
    store = stock_level.store

    data = {"amount": 0, "product_id": product.id, "store_id": store.id}
    response = client.post(f"{settings.API_V1_STR}/stock_levels/", json=data,)

    assert response.status_code == 400


def test_read_stock_level(client: TestClient, db: Session) -> None:
    stock_level = create_random_stock_level(db)
    response = client.get(f"{settings.API_V1_STR}/stock_levels/{stock_level.id}",)

    assert response.status_code == 200
    content = response.json()
    assert content["amount"] == stock_level.amount
    assert content["id"] == stock_level.id


def test_delete_stock_level(client: TestClient, db: Session) -> None:
    stock_level = create_random_stock_level(db)
    response = client.delete(f"{settings.API_V1_STR}/stock_levels/{stock_level.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == stock_level.id

    stock_level2 = crud.stock_level.get(db=db, id=stock_level.id)
    assert not stock_level2
