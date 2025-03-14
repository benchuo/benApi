## test explanation

We're testing the following API endpoints:

* **Books:**
    * `GET /books`
    * `POST /books`
    * `PUT /books/{book_id}`
    * `DELETE /books/{book_id}`
* **Users:**
    * `GET /users`
    * `POST /users/{user_id}/borrow/{book_id}`
    * `POST /users/{user_id}/return/{book_id}`

Im executing both negative and positive test scenarios

## Test Scenarios and Assertions

* Verify the API returns a list of all books. (GET /books - Asserts a 200 status code and a JSON response containing a list of books.)
* Verify a new book can be added to the system. (POST /books - Asserts a 201 status code and a JSON response containing the newly added book.)
* Verify the details of an existing book can be updated. (PUT /books/{book_id} - Asserts a 200 status code and a JSON response with the updated book details.)
* Verify a book can be removed from the system (DELETE /books/{book_id} - Asserts a 200 status code and a success message.)
* Verify the API returns a list of all users. (GET /users - Asserts a 200 status code and a JSON response containing a list of users.)
* Verify a user can successfully borrow a book. (POST /users/{user_id}/borrow/{book_id} - Asserts a 200 status code and a success message.)
* Verify a user can successfully return a book. (POST /users/{user_id}/return/{book_id} - Asserts a 200 status code and a success message.)
* Verify the API returns a 400 error when attempting to add a book with missing information. (POST /books - negative test - Asserts a 400 status code and an error message in the JSON response.)
* Verify the API returns a 404 error when attempting to update or delete a non-existent book. (PUT/DELETE /books/{book_id} - negative tests - Asserts a 404 status code and an error message in the JSON response.)
* Verify the API returns a 404 error when a user attempts to borrow a non-existent book. (POST /users/{user_id}/borrow/{book_id} - negative test - Asserts a 404 status code and an error message in the JSON response.)
* Verify the API returns a 400 error when a user attempts to return a book they did not borrow. (POST /users/{user_id}/return/{book_id} - negative test - Asserts a 400 status code and an error message in the JSON response.)

# How It Works

im using:

* pytest: To run our tests and report the results.
* requests: To send HTTP requests to the API.
* Flask: To simulate the API (if running locally).
* Helper functions in `utils/helpers.py` to create test data, which makes the tests less repetitive.
