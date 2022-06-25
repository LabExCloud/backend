## Lab Exam

use request header:  
```http
Authorization: "Token <token>"
```

- Get all exams in lab c_id  
`GET    /api/v1/labexams/<int:c_id>`

    response:
    ```js
    [
        {
            "id": Number,
            "questions": [
                {
                    "id": Number,
                    "testcases": [],
                    "title": String,
                    "question": String,
                    "answer": String,
                    "mark": Number,
                    "language": Number
                },
                ...
            ],
            "subject": String,
            "exam_name": String,
            "created": String,
            "modified": String,
            "start_date": String,
            "due_date": String,
            "total_marks": Number
        },
        ...
    ]
    ```

- Get detail of lab exam e_id  
`GET    /api/v1/labexams/exam/<int:e_id>`

    response:
    ```js
    {
        "id": Number,
        "questions": [
            {
                "id": Number,
                "testcases": [],
                "title": String,
                "question": String,
                "answer": String,
                "mark": Number,
                "language": Number
            },
            ...
        ],
        "subject": String,
        "exam_name": String,
        "created": String,
        "modified": String,
        "start_date": String,
        "due_date": String,
        "total_marks": Number
    }
    ```

- Get detail of question q_id  
`GET    /api/v1/labexams/question/<int:q_id>`

### Student
- List all lab exams in current semester  
`GET    /api/v1/labs`

- List all lab exams in a semester sem  
`GET    /api/v1/labs/sem/<int:sem>`

- Add answer for the question q_id  
`POST   /api/v1/labexams/answer/<int:q_id>`


### Teacher
- create a lab exam in the class class_id  
`POST   /api/v1/labexams/exam/t:class_id>`

    request:
    ```js
    {
        "exam_name": String,
        "start_date": String,
        "due_date": String,
        "total_marks": Number
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "questions": [],
        "subject": String,
        "exam_name": String,
        "created": String,
        "modified": String,
        "start_date": String,
        "due_date": String,
        "total_marks": Number
    }
    ```

- update a lab exam e_id  
`PUT    /api/v1/labexams/exam/t:e_id>`

    request & response:  
    same as above

- delete a lab exam e_d  
`DELETE  /api/v1/labexams/exam/t:e_id>`

- create a question for lab exam e_id  
`POST    /api/v1/labexams/question/<int:e_id>`  

- edit a question q_id  
`PUT     /api/v1/labexams/question/<int:q_id>`  

- delete a question q_id  
`DELETE  /api/v1/labexams/question/<int:q_id>`  

- add a testcase for question q_id  
`POST    /api/v1/labexams/testcase/<int:q_id>`

- edit testcase t_id  
`PUT     /api/v1/labexams/testcase/<int:t_id>`

- delete testcase t_id  
`DELETE  /api/v1/labexams/testcase/<int:t_id>`

Refer LabAPI.md for headers, request and response for question, answer and testcase.