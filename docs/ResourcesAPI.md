## Resources

use request header:  
```http
Authorization: "Token <token>"
```

- Get detailed data of resource r_id  
`GET    /api/v1/resources/res/<int:r_id>`

    response:
    ```js
    {
        "id": Number,
        "res_name": String,
        "description": String,
        "created": String,  // eg:- "2022-04-24T09:36:26.423130Z"
        "modified": String, // eg:- "2022-04-24T09:36:26.423130Z"
        "res_files": [
            {
                "id": Number,
                "file": String,
                "filename": String
            },
            ...
        ]
    }
    ```

- list of resources in a class class_id  
`GET    /api/v1/resources/class/<int:class_id>`  

    response:
    ```js
    {
        "id": Number,
        "res_name": String,
        "description": String,
        "created": String,  // eg:- "2022-04-24T09:36:26.423130Z"
        "modified": String, // eg:- "2022-04-24T09:36:26.423130Z"
        "class_a": Number
    }
    ```

### Student
- List all resources in current semester  
`GET    /api/v1/resources`

    response:
    ```js
    [
        {
            "id": Number,
            "sub_name": String,
            "sub_code": String,
            "sem": Number,
            "resources": [
                {
                    "id": Number,
                    "res_name": String,
                    "description": String,
                    "created": String,  // eg:- "2022-04-24T09:36:26.423130Z"
                    "modified": String, // eg:- "2022-04-24T09:36:26.423130Z"
                    "class_a": Number
                },
                ...
            ]
        },
        ...
    ]
    ```

- List all resources in a semester sem  
`GET    /api/v1/resources/sem/<int:sem>`

    response: same as above


### Teacher
- create a resource in the class class_id  
`POST   /api/v1/resources/res/<int:class_id>`

    request:
    ```js
    {
        "res_name": String,  
        "description": String,  
    }
    ``` 

    response: 
    ```js
    {
        "id": Number,
        "res_name": String,
        "description": String,
        "created": String,        // eg:- "2022-04-24T09:36:26.423130Z"
        "modified": String,       // eg:- "2022-04-24T09:36:26.423130Z"
    }
    ```

- update a resource r_id  
`PUT    /api/v1/resources/res/<int:r_id>`

    request:
    ```js
    {
        "res_name": String,
        "description": String,
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "res_name": String,
        "description": String,
        "created": String,        // eg:- "2022-04-24T09:36:26.423130Z"
        "modified": String,       // eg:- "2022-04-24T09:36:26.423130Z"
    }
    ```

- delete a resource r_d  
`DELETE  /api/v1/resources/res/<int:r_id>`  

    NOTE: deleting a resource also deletes its resource files


- create a resource file for resource r_id  
`POST    /api/v1/resources/file/<int:r_id>` 

    header:
    ```http
    Content-Type: "multipart/form-data"
    ```
    
    request:
    ```js
    {
        "file": File
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "file": String,       // eg: "/media/uploads/resources/file.pdf"
        "filename": String
    }
    ```

- edit a resource file  
`PUT     /api/v1/resources/file/<int:rf_id>`  

    header:
    ```http
    Content-Type: "multipart/form-data"
    ```
    
    request:
    ```js
    {
        "file": File
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "file": String,       // eg: "/media/uploads/resources/file.pdf"
        "filename": String
    }
    ```

- delete a resource file  
`DELETE  /api/v1/resources/file/<int:rf_id>`  