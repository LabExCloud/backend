## Class

use request header:  
```http
Authorization: "Token <token>"
```

- list all classes a user has  
`GET    /api/v1/classes`

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
            ],
            is_lab: Boolean
        },
        ...
    ]
    ```
    

- view a class c_id  
`GET    /api/v1/class/<int:c_id>`

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
        ],
        is_lab: Boolean
    }
    ```

- create a class  
`POST    /api/v1/class`

    request:
    ```js
    {
        "department": Number,
        "semester": Number,
        "subject": Number,
        "batch": Number,
        "teachers": [Number, ...],  // optional
        "is_lab": Boolean           // optional, default false
    }
    ```

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
        ],
        is_lab: Boolean
    }
    ```

- modify a class c_id  
`PUT    /api/v1/class/<int:c_id>`

    request:
    ```js
    {
        "department": Number,
        "semester": Number,
        "subject": Number,
        "batch": Number,
        "teachers": [Number, ...],
        "is_lab": Boolean
    }
    ```

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
        ],
        is_lab: Boolean
    }
    ```

- delete a class c_id  
`DELETE    /api/v1/class/<int:c_id>`

- List all students in a class c_id
`GET    /api/v1/class/students/<int:c_d>`

    response:
    ```js
    [
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