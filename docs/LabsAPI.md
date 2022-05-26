## Labs

use request header:  
```http
Authorization: "Token <token>"
```

- Get all experiment in lab c_id  
`GET    /api/v1/labs/<int:id>`

    response:
    ```js
    [
        {
            "id": Number,
            "questions": [],
            "subject": String,
            "exp_name": "hello, world",
            "created": String,  // eg:- "2022-04-24T09:36:26.423130Z"
            "modified": String, // eg:- "2022-04-24T09:36:26.423130Z"
            "due_date": String, // eg:- "2022-04-24T09:36:26.423130Z"
            "total_marks": Number
        },
        ...
    ]
    ```

- Get detail of experiment e_id  
`GET    /api/v1/labs/exp/<int:e_id>`

    response:
    ```js
    {
        "id": Number,
        "questions": [],
        "exp_name": "hello, world",
        "created": String,  // eg:- "2022-04-24T09:36:26.423130Z"
        "modified": String, // eg:- "2022-04-24T09:36:26.423130Z"
        "due_date": String, // eg:- "2022-04-24T09:36:26.423130Z"
        "total_marks": Number
    }
    ```

- Get detail of question q_id  
`GET    /api/v1/labs/question/<int:q_id>`

    response:
    ```js
    {
        "id": Number,
        "testcases": [],
        "question_number": Number,
        "question": String,
        "answer": String,
        "language": Number,
        "mark": Number
    }
    ```

- Get testcase tc_id  
`GET    /api/v1/labs/testcase/<int:tc_id>`

    response:
    ```js
    {
        "id": Number,
        "tc_number": Number,
        "hidden": Boolean,
        "input_file": String,
        "output_file": "String,
        "mark": Number
    }
    ```


### Student
- List all labs for current student  
`GET    /api/v1/labs`

    response:
    ```js
    [
        {
            "id": Number,
            "department": Number,
            "semester": Number,
            "subject": Number,
            "batch": Number,
            "owner": Number,
            "teachers": [
                Number,
                ...
            ],
            "is_lab": Boolean
        },
        ...
    ]
    ```

- List all labs in current semester  
`GET    /api/v1/labs/sem`

    response: same as above

- List all labs in a semester sem  
`GET    /api/v1/labs/sem/<int:sem>`

    response: same as above


- View answer for the answer a_id
`GET    /api/v1/labs/answer/<int:a_id>`

    response:
    ```js
    {
        "id": Number,
        "answer": String,
        "submitted": String,
        "modified": String,
        "execution_tries": Number,
        "execution_time": Number,
        "total_marks": Number,
        "question": Number,
        "student": Number
    }
    ```

- Add answer for the question q_id  
`POST   /api/v1/labs/answer/<int:q_id>`

    request:
    ```js
    {
        execution_tries: Number,
        execution_time: Number,
        total_marks: Number,
        answer: File
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "answer": String,
        "submitted": String,
        "modified": String,
        "execution_tries": Number,
        "execution_time": Number,
        "total_marks": Number,
        "question": Number,
        "student": Number
    }
    ```

- Edit answer a_id  
`PUT    /api/v1/labs/answer/<int:qa_id>`

    request & response:  
    same as above

- Delete answer a_id  
`DELETE /api/v1/labs/answer/<int:qa_id>`


### Teacher
- create an experiment in the class class_id  
`POST   /api/v1/labs/exp/<int:class_id>`

    request:
    ```js
    {
        "exp_name": String,
        "total_marks": Number,
        "due_date": String
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "questions": [],
        "exp_name": "hello, world",
        "created": String,  // eg:- "2022-04-24T09:36:26.423130Z"
        "modified": String, // eg:- "2022-04-24T09:36:26.423130Z"
        "due_date": String, // eg:- "2022-04-24T09:36:26.423130Z"
        "total_marks": Number
    }
    ```

- update an experiment e_id  
`PUT    /api/v1/labs/exp/<int:e_id>`

    request & response: same as above

- delete an experiment e_d  
`DELETE  /api/v1/labs/exp/<int:e_id>`

- create a question for experiment e_id  
`POST    /api/v1/labs/question/<int:e_id>`
    
    request:
    ```js
    {
        "experiment": Number,
        "question_number": Number,
        "title": String,
        "question": String,
        "language": Number,
        "mark": Number
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "testcases": [],
        "question_number": Number,
        "title": String,
        "question": String,
        "answer": String,
        "language": Number,
        "mark": Number
    }
    ```

- edit a question q_id  
`PUT     /api/v1/labs/question/<int:q_id>`  
    
    request:
    ```js
    {
        "experiment": Number,
        "question_number": Number,
        "title": String,
        "question": String,
        "language": Number,
        "mark": Number
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "testcases": [],
        "question_number": Number,
        "title": String,
        "question": String,
        "answer": String,
        "language": Number,
        "mark": Number
    }
    ```

- delete a question q_id  
`DELETE  /api/v1/labs/question/<int:q_id>`  

- add a testcase for question q_id  
`POST    /api/v1/labs/testcase/<int:q_id>`

    header:
    ```http
    Content-Type: "multipart/form-data"
    ```
    
    request:
    ```js
    {
        "input_file": File,
        "output_file": File,
        "mark": Number    
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "hidden": Boolean,
        "input_file": String,   // eg: "/media/uploads/lab/testcase/input/in.txt"
        "output_file": String,  // eg: "/media/uploads/lab/testcase/input/out.txt"
        "mark": Number
    }

- edit testcase t_id  
`PUT     /api/v1/labs/testcase/<int:t_id>`

    header:
    ```http
    Content-Type: "multipart/form-data"
    ```
    
    request:
    ```js
    {
        "input_file": File,
        "output_file": File,
        "mark": Number    
    }
    ```

    response:
    ```js
    {
        "id": Number,
        "hidden": Boolean,
        "input_file": String,   // eg: "/media/uploads/lab/testcase/input/in.txt"
        "output_file": String,  // eg: "/media/uploads/lab/testcase/input/out.txt"
        "mark": Number
    }

- delete testcase t_id  
`DELETE  /api/v1/labs/testcase/<int:t_id>`


- list all answers of question q_id
`GET    /api/v1/labs/answers/<int:q_id>`

    response:
    ```js
    [
        {
            "id": Number,
            "answer": String,
            "submitted": String,
            "modified": String,
            "execution_tries": Number,
            "execution_time": Number,
            "total_marks": Number,
            "question": Number,
            "student": Number
        },
        ...
    ]
    ```

- View answer for the answer a_id
`GET    /api/v1/labs/answer/<int:a_id>`

    response:
    ```js
    {
        "id": Number,
        "answer": String,
        "submitted": String,
        "modified": String,
        "execution_tries": Number,
        "execution_time": Number,
        "total_marks": Number,
        "question": Number,
        "student": Number
    }
    ```