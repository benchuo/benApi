import pytest
import requests
import uuid

BASE_URL = "http://127.0.0.1:5000"

def test_get_books():
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200

def test_add_book_success():
    book_data = {"title": "Test Book", "author": "Test Author"}
    response = requests.post(f"{BASE_URL}/books", json=book_data)
    assert response.status_code == 201

def test_add_book_failure_missing_title():
    book_data = {"author": "Test Author"}
    response = requests.post(f"{BASE_URL}/books", json=book_data)
    assert response.status_code == 400
    assert "error" in response.json()

def test_update_book_success():
    book_data = {"title": "Updated Title", "author": "Updated Author"}
    response_post = requests.post(f"{BASE_URL}/books", json={"title": "Original Title", "author": "Original Author"})
    book_id = response_post.json()["id"]
    response = requests.put(f"{BASE_URL}/books/{book_id}", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_update_book_failure_not_found():
    response = requests.put(f"{BASE_URL}/books/{uuid.uuid4()}", json={"title": "Updated Title"})
    assert response.status_code == 404
    assert "error" in response.json()

def test_delete_book_success():
    response_post = requests.post(f"{BASE_URL}/books", json={"title": "ToDelete", "author": "ToDelete Author"})
    book_id = response_post.json()["id"]
    response = requests.delete(f"{BASE_URL}/books/{book_id}")
    assert response.status_code == 200

def test_delete_book_failure_not_found():
    response = requests.delete(f"{BASE_URL}/books/{uuid.uuid4()}")
    assert response.status_code == 404
    assert "error" in response.json()