from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.tests.utils.store import create_random_store
from app.tests.utils.utils import random_lower_string


def test_read_stores(client: TestClient, db: Session) -> None:
    store = create_random_store(db)
    # this will fail if the test-database is never cleaned up
    limit = int(1e6)
    response = client.get(f"{settings.API_V1_STR}/stores?limit={limit}")
    assert response.status_code == 200
    content = response.json()

    found_store = None
    for store_in_result in content:
        if store.id == store_in_result["id"]:
            found_store = store_in_result
            break

    assert found_store
    assert found_store["code"] == store.code


def test_create_store(client: TestClient, db: Session) -> None:
    code = random_lower_string()
    data = {"code": code}
    response = client.post(f"{settings.API_V1_STR}/stores/", json=data,)
    assert response.status_code == 200
    content = response.json()
    assert content["code"] == data["code"]
    assert "id" in content


def test_fail_on_create_duplicate_store(client: TestClient, db: Session) -> None:
    store = create_random_store(db)
    data = {"code": store.code}

    response = client.post(f"{settings.API_V1_STR}/stores/", json=data,)

    assert response.status_code == 400


def test_read_store(client: TestClient, db: Session) -> None:
    store = create_random_store(db)
    response = client.get(f"{settings.API_V1_STR}/stores/{store.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["code"] == store.code
    assert content["id"] == store.id


def test_delete_store(client: TestClient, db: Session) -> None:
    store = create_random_store(db)
    response = client.delete(f"{settings.API_V1_STR}/stores/{store.id}",)
    assert response.status_code == 200
    content = response.json()
    assert content["code"] == store.code
    assert content["id"] == store.id

    store2 = crud.store.get(db=db, id=store.id)
    assert not store2
