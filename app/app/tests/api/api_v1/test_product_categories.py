from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.tests.utils.product_category import create_random_product_category
from app.tests.utils.utils import random_lower_string


def test_read_product_categories(client: TestClient, db: Session) -> None:
    category = create_random_product_category(db)
    # this will fail if the test-database is never cleaned up
    limit = int(1e6)
    response = client.get(f"{settings.API_V1_STR}/product_categories?limit={limit}",)
    assert response.status_code == 200
    content = response.json()

    found_category = None
    for category_in_result in content:
        if category.id == category_in_result["id"]:
            found_category = category_in_result
            break

    assert found_category
    assert found_category["name"] == category.name


def test_create_product_category(client: TestClient, db: Session) -> None:
    name = random_lower_string()
    data = {"name": name}
    response = client.post(f"{settings.API_V1_STR}/product_categories/", json=data,)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_fail_on_create_duplicate_store(client: TestClient, db: Session) -> None:
    category = create_random_product_category(db)
    data = {"name": category.name}

    response = client.post(f"{settings.API_V1_STR}/product_categories/", json=data,)

    assert response.status_code == 400


def test_read_product_category(client: TestClient, db: Session) -> None:
    category = create_random_product_category(db)
    response = client.get(f"{settings.API_V1_STR}/product_categories/{category.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == category.name
    assert content["id"] == category.id


def test_delete_product_category(client: TestClient, db: Session) -> None:
    category = create_random_product_category(db)
    response = client.delete(f"{settings.API_V1_STR}/product_categories/{category.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == category.name
    assert content["id"] == category.id

    category2 = crud.product_category.get(db=db, id=category.id)
    assert not category2
