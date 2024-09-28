
# User Management Service

The User Management Service is a part of the Personal Finance Tracker application. It handles user-related operations such as creating, updating, retrieving, and deleting user information.

## Features

- Create new users
- Retrieve existing users
- Update user information
- Delete users

## Technologies Used

- Python 3.9
- Flask
- DynamoDB (AWS)
- Boto3 (AWS SDK for Python)

## API Endpoints

### Create User

- **POST** `/users`
- **Request Body:**
  ```json
  {
    "username": "johndoe",
    "email": "johndoe@example.com"
  }
  
- **Response:**
  ```
  {
    "message": "User created successfully",
    "user_id": "abc123"
  }

- **GET** `/users`
- **Response:**
    ```
      {
        "user_id": "abc123",
        "username": "johndoe",
        "email": "johndoe@example.com"
      },
      {
        "user_id": "def456",
        "username": "janedoe",
        "email": "janedoe@example.com"
      }

- **Update User**

- **PUT** `/users/<user_id>`
- **Request Body:**
    ```
    {
     "username": "johnsmith",
     "email": "johnsmith@example.com"
    }

- **Response:**
   ```
   {
     "message": "User updated successfully"
   }

- **Delete User**

- **DELETE** `/users/<user_id>`
- **Response:**
    ```
    {
    "message": "User deleted successfully"
    }
  

