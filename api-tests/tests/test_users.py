import pytest
import requests
import uuid

BASE_URL = "http://127.0.0.1:5000"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_borrow_book_success():
    response_post_book = requests.post(f"{BASE_URL}/books", json={"title": "Borrow Test", "author": "Borrow Author"})
    book_id = response_post_book.json()["id"]
    response_post_user = requests.post(f"{BASE_URL}/users", json={"name": "Borrow User"})
    user_id = response_post_user.json()["id"]
    response = requests.post(f"{BASE_URL}/users/{user_id}/borrow/{book_id}")
    assert response.status_code == 200

def test_borrow_book_failure_book_not_found():
    response_post_user = requests.post(f"{BASE_URL}/users", json={"name": "Borrow User"})
    user_id = response_post_user.json()["id"]
    response = requests.post(f"{BASE_URL}/users/{user_id}/borrow/{uuid.uuid4()}")
    assert response.status_code == 404
    assert "error" in response.json()

def test_return_book_success():
    response_post_book = requests.post(f"{BASE_URL}/books", json={"title": "Return Test", "author": "Return Author"})
    book_id = response_post_book.json()["id"]
    response_post_user = requests.post(f"{BASE_URL}/users", json={"name": "Return User"})
    user_id = response_post_user.json()["id"]
    requests.post(f"{BASE_URL}/users/{user_id}/borrow/{book_id}")
    response = requests.post(f"{BASE_URL}/users/{user_id}/return/{book_id}")
    assert response.status_code == 200

def test_return_book_failure_book_not_borrowed():
    response_post_book = requests.post(f"{BASE_URL}/books", json={"title": "Return Test", "author": "Return Author"})
    book_id = response_post_book.json()["id"]
    response_post_user = requests.post(f"{BASE_URL}/users", json={"name": "Return User"})
    user_id = response_post_user.json()["id"]
    response = requests.post(f"{BASE_URL}/users/{user_id}/return/{book_id}")
    assert response.status_code == 400
    assert "error" in response.json()