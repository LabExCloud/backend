## Analysis

use request header:  
```http
Authorization: "Token <token>"
```

- Get student (sid) report of experiments in a class (cid)  
`GET    /api/v1/analysis/report/<int:cid>/<int:sid>`

    response:
    ```js
    [
        {
            "exp_name": String,
            "exp_id": Number,
            "total_questions": Number,
            "completed": Number,
            "submited_ontime": Number
        },
        ...
    ]
    ```