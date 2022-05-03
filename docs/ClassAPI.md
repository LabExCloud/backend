## Class

use request header:  
```http
Authorization: "Token <token>"
```

- list all classes a user has  
`GET    /api/v1/classes`

    response:
    ```js
    {
        "id": Number,
        "department": {
            "id": Number,
            "dept_name": String,
            "dept_code": String
        },
        "semester": {
            "id": Number,
            "sem": Number
        },
        "subject": {
            "id": Number,
            "sub_name": String,
            "sub_code": String,
            "image": String
        },
        "batch": {
            "id": Number,
            "year": Number,
            "stream": String
        },
        "owner": {
            "id": Number,
            "username": String,
            "first_name": String,
            "last_name": String,
            "email": String,
            "phone": String
        },
        "teachers": [
            {
            "id": Number,
            "username": String,
            "first_name": String,
            "last_name": String,
            "email": String,
            "phone": String
            }
            ...
        ]
    }
    ```
    

- view a class c_id  
`GET    /api/v1/class/<int:c_id>`

    response:
    ```js
    [
        {
            "id": Number,
            "department": {
                "id": Number,
                "dept_name": String,
                "dept_code": String
            },
            "semester": {
                "id": Number,
                "sem": Number
            },
            "subject": {
                "id": Number,
                "sub_name": String,
                "sub_code": String,
                "image": String
            },
            "batch": {
                "id": Number,
                "year": Number,
                "stream": String
            },
            "owner": {
                "id": Number,
                "username": String,
                "first_name": String,
                "last_name": String,
                "email": String,
                "phone": String
            },
            "teachers": [
                {
                "id": Number,
                "username": String,
                "first_name": String,
                "last_name": String,
                "email": String,
                "phone": String
                },
                ...
            ]
        },
        ...
    ]
    ```