import requests

def create_book(base_url, title, author):
    book_data = {"title": title, "author": author}
    response = requests.post(f"{base_url}/books", json=book_data)
    return response.json()["id"]

def create_user(base_url, name):
    user_data = {"name": name}
    response = requests.post(f"{base_url}/users", json=user_data)
    return response.json()["id"]

def borrow_book(base_url, user_id, book_id):
    response = requests.post(f"{base_url}/users/{user_id}/borrow/{book_id}")
    return response.status_code

def return_book(base_url, user_id, book_id):
    response = requests.post(f"{base_url}/users/{user_id}/return/{book_id}")
    return response.status_code