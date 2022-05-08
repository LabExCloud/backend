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
`GET   /api/v1/profile`

    request header:
    ```http
    Authorization: "Token <token>"
    ```

    - Student  
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
                "id": Number,
                "dept_name": String,
                "dept_code": String,
                "semester": Number,
                "semesters": [
                    Number,
                    ...
                ],
                "rollno": Number,
                "year": Number,
                "stream": String,
                "classes": [
                    Number,
                    ...
                ]
            },
            "user_type": String    // 'student', 'teacher', 'admin'
        }
        ```

    - Teacher  
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
                "id": Number,
                "dept_name": String,
                "dept_code": String,
                "classes": [
                    Number,
                    ...
                ]
            },
            "user_type": String    // 'student', 'teacher', 'admin'
        }
        ```