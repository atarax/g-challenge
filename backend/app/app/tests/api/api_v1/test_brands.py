from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.brand import create_random_brand
from app.tests.utils.utils import random_lower_string


def test_read_brands(client: TestClient, db: Session) -> None:
    brand = create_random_brand(db)
    # this will fail if the test-database is never cleaned up
    limit = int(1e6)
    response = client.get(f"{settings.API_V1_STR}/brands?limit={limit}",)
    assert response.status_code == 200
    content = response.json()

    found_brand = False
    for brand_in_result in content:
        if brand.id == brand_in_result["id"]:
            found_brand = brand_in_result
            break

    assert found_brand
    assert found_brand["name"] == brand.name


def test_create_brand(client: TestClient, db: Session) -> None:
    name = random_lower_string()
    data = {"name": name}
    response = client.post(f"{settings.API_V1_STR}/brands/", json=data,)

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_fail_on_create_duplicate_brand(client: TestClient, db: Session) -> None:
    brand = create_random_brand(db)
    data = {"name": brand.name}
    response = client.post(f"{settings.API_V1_STR}/brands/", json=data,)

    assert response.status_code == 400


def test_read_brand(client: TestClient, db: Session) -> None:
    brand = create_random_brand(db)
    response = client.get(f"{settings.API_V1_STR}/brands/{brand.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == brand.name
    assert content["id"] == brand.id
