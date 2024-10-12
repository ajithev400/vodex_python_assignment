
# API Documentation for vodex.ai

## Base URL
`http://127.0.0.1:8000/api/v1`

### Endpoints

---

### 1. Create Item

- **Endpoint:** `POST /items/`
- **Description:** Creates a new item.
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "email": "john@example.com",
        "item_name": "Milk",
        "quantity": 5,
        "expiry_date": "2024-12-31"
    }
    ```
- **Example Request:**
    ```
    POST http://127.0.0.1:8000/api/v1/items/
    ```

---

### 2. Get Item

- **Endpoint:** `GET /items/<id>`
- **Description:** Retrieves an existing item by its ID.
- **Example Request:**
    ```
    GET http://127.0.0.1:8000/api/v1/items/67096bb575e99733270da38d
    ```

--- 

### 3. Delete Item

- **Endpoint:** `DELETE /items/<id>`
- **Description:** Deletes an existing item by its ID.
- **Example Request:**
    ```
    DELETE http://127.0.0.1:8000/api/v1/items/67096aad94ca9bac9458d99e
    ```

---

### 4. Update Item

- **Endpoint:** `PUT /items/<id>`
- **Description:** Updates an existing item by its ID.
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "email": "UPDATEjohn@example.com",
        "item_name": "rice",
        "quantity": 8,
        "expiry_date": "2024-12-31"
    }
    ```
- **Example Request:**
    ```
    PUT http://127.0.0.1:8000/api/v1/items/67096a4894ca9bac9458d99d
    ```

---

### 5. Create User

- **Endpoint:** `POST /users/`
- **Description:** Creates a new user.
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "SuperSecretPassword"
    }
    ```
- **Example Request:**
    ```
    POST http://127.0.0.1:8000/api/v1/users/
    ```

---

### 6. Get User

- **Endpoint:** `GET /users/<id>`
- **Description:** Retrieves an existing user by their ID.
- **Example Request:**
    ```
    GET http://127.0.0.1:8000/api/v1/users/670a17acdfea14dd2cf9e916
    ```

---

### 7. Create Clock In Record

- **Endpoint:** `POST /clockin/`
- **Description:** Creates a new clock-in record for a user.
- **Request Body:**
    ```json
    {
        "user_id": "670a17acdfea14dd2cf9e916",
        "email": "john.doe@example.com",
        "location": "Office"
    }
    ```
- **Example Request:**
    ```
    POST http://127.0.0.1:8000/api/v1/clockin/
    ```

---

### 8. Get Clock-in Records

- **Endpoint:** `GET /clockin/<id>`
- **Description:** Retrieves an existing clock-in records by their ID

- **Example Request:**
    ```
    POST http://127.0.0.1:8000/api/v1/clockin/<id>
    ```

---


## Notes

- Replace `<id>` with the actual ID of the item or user you wish to interact with.
- Ensure that the server is running on `http://127.0.0.1:8000` before making requests.
- The API supports JSON format for requests and responses.
