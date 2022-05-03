## User

### Authentication

- Authenticate and get token  
`POST   /api/v1/token/login`

    request data: 
    ```js
    {
        username: String,
        password: String
    }
    ```

    response data:
    ```js
    {
        "auth_token": String
    }
    ```

### User Profile

- Get user profile
    request header:
    ```http
    Authorization: "Token <token>"
    ```

    response data:
    ```js
    {
        "id": Number,
        "username": String,
        "first_name": String,
        "middle_name": String,
        "last_name": String,
        "email": String,
        "phone": String,
        "get_image": String,
        "profile": {
            "dept_name": String,
            "dept_code": String,
            "semester": Number,
            "semesters": [
                Number,
                ...
            ],
            "rollno": Number,
            "year": Number,
            "stream": String
        },
        "user_type": String    // 'student', 'teacher', 'admin'
    }