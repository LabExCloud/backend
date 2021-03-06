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
                "department: {
                    "id" : Number,
                    "dept_name": String,
                    "dept_code": String,
                }
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
            "image": String,
            "profile": {
                "id": Number,
                "department: {
                    "id" : Number,
                    "dept_name": String,
                    "dept_code": String,
                }
                "classes": [
                    Number,
                    ...
                ]
            },
            "user_type": String    // 'student', 'teacher', 'admin'
        }
        ```

- Change password  
`PUT    /api/v1/password`

    request:
    ```js
    {
        "password": String
    }
    ```

- Change Profile Image  
`PUT    /api/v1/profileimage`

    header:
    ```http
    Content-Type: "multipart/form-data"
    ```

    request:
    ```js
    {
        "image": File
    }
    ```

## Teacher
- List all students
`GET    /api/v1/students`

    response:
    ```js
    [
        {
            "id": Number,
            "username": String,
            "first_name": String,
            "last_name": String,
            "email": String,
            "phone": String,
            "student": Number
        },
        ...
    ]

- List all teachers
`GET    /api/v1/teachers`

    response:
    ```js
    [
        {
            "id": Number,
            "username": String,
            "first_name": String,
            "last_name": String,
            "email": String,
            "phone": String,
            "teacher": Number
        },
        ...
    ]

- Create Student Accounts from csv file
`POST   /api/v1/students/csv`

    header:
    ```http
    Content-Type: "multipart/form-data"
    ```
    
    request:
    ```js
    {
        "file": File    // csv file:  rollno,username,password,firstname,middlename,lastname,email,phone,semester,stream,year
    }
    ```

- Delete Student sid
`DELETE /api/v1/student/<int:sid>`