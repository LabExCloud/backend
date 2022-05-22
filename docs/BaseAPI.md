## Base

- Get all Batches List  
`GET    /api/v1/base/batches`

    response:
    ```js
    {
        "id": Number,
        "year": Number,
        "stream": String
    }
    ```

- Get all Subjects List  
`GET    /api/v1/base/subjects`

    response:
    ```js
    [
        {
            "id": Number,
            "sub_name": String,
            "sub_code": String,
            "image": String
        },
        ...
    ]
    ```