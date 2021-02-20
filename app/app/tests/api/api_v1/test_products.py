from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.tests.utils.brand import create_random_brand
from app.tests.utils.product import create_random_product
from app.tests.utils.product_category import create_random_product_category
from app.tests.utils.utils import random_lower_string


def test_read_products(client: TestClient, db: Session) -> None:
    product = create_random_product(db)
    # this will fail if the test-database is never cleaned up
    limit = int(1e6)
    response = client.get(f"{settings.API_V1_STR}/products?limit={limit}",)
    assert response.status_code == 200
    content = response.json()

    found_product = None
    for product_in_result in content:
        if product.id == product_in_result["id"]:
            found_product = product_in_result
            break

    assert found_product
    assert found_product["name"] == product.name


def test_create_product(client: TestClient, db: Session) -> None:
    name = random_lower_string()
    category = create_random_product_category(db)
    brand = create_random_brand(db)

    data = {"name": name, "category_id": category.id, "brand_id": brand.id}
    response = client.post(f"{settings.API_V1_STR}/products/", json=data,)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_fail_on_create_duplicate_product(client: TestClient, db: Session) -> None:
    product = create_random_product(db)
    category = create_random_product_category(db)
    brand = create_random_brand(db)

    data = {"name": product.name, "category_id": category.id, "brand_id": brand.id}
    response = client.post(f"{settings.API_V1_STR}/products/", json=data,)

    assert response.status_code == 400


def test_read_product(client: TestClient, db: Session) -> None:
    product = create_random_product(db)
    response = client.get(f"{settings.API_V1_STR}/products/{product.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == product.name
    assert content["id"] == product.id


def test_delete_product(client: TestClient, db: Session) -> None:
    product = create_random_product(db)
    response = client.delete(f"{settings.API_V1_STR}/products/{product.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == product.name
    assert content["id"] == product.id

    product2 = crud.product.get(db=db, id=product.id)
    assert not product2
