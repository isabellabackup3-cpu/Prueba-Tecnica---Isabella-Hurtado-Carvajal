# pytest tests for FakeStoreAPI
import os
import json
import pytest
import requests

BASE_URL = os.getenv("FAKESTORE_BASE_URL", "https://fakestoreapi.com")

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s

@pytest.fixture(scope="session")
def new_product(session):
    """Create a product and yield its id for update tests; then cleanup (best-effort)."""
    payload = {
        "title": "Your Store Test Product",
        "price": 19.99,
        "description": "Created by automated tests",
        "image": "https://i.pravatar.cc/300?img=1",
        "category": "electronics"
    }
    r = session.post(f"{BASE_URL}/products", data=json.dumps(payload), timeout=30)
    assert r.status_code in (200, 201), f"POST failed: {r.status_code} {r.text}"
    body = r.json()
    prod_id = body.get("id") or body.get("result", {}).get("id")
    assert prod_id, f"Response had no id: {body}"
    yield prod_id

    # Cleanup (ignore failures; FakeStore may not persist)
    try:
        session.delete(f"{BASE_URL}/products/{prod_id}", timeout=15)
    except Exception:
        pass

def test_list_electronics(session):
    r = session.get(f"{BASE_URL}/products/category/electronics", timeout=30)
    assert r.status_code == 200, r.text
    items = r.json()
    assert isinstance(items, list) and len(items) > 0, "Expected non-empty list"
    for item in items:
        assert item.get("category") == "electronics", f"Wrong category: {item.get('category')}"

def test_get_product_by_id(session):
    # using id=1 as a known example
    r = session.get(f"{BASE_URL}/products/1", timeout=30)
    assert r.status_code == 200, r.text
    body = r.json()
    for key in ("id", "title", "price", "category", "image"):
        assert key in body, f"Missing key {key}"

def test_create_product(session, new_product):
    assert isinstance(new_product, int), "id should be int"

def test_update_product_image(session, new_product):
    new_img = "https://i.pravatar.cc/300?img=2"
    payload = {"image": new_img}
    r = session.put(f"{BASE_URL}/products/{new_product}", data=json.dumps(payload), timeout=30)
    assert r.status_code in (200, 201), r.text
    body = r.json()
    assert body.get("image") == new_img, f"Image not updated: {body.get('image')}"
