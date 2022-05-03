## Labs

- Get all experiment in lab c_id  
`GET    /api/v1/labs/exps/<int:c_id>`

- Get detail of experiment e_id  
`GET    /api/v1/labs/exp/<int:e_id>`

### Student
- List all labs in current semester  
`GET    /api/v1/labs`

- List all labs in a semester sem  
`GET    /api/v1/labs/sem/<int:sem>`

&cross; Add answer for the question q_id  
`POST   /api/v1/labs/answer/<int:q_id>`

&cross; Edit answer a_id  
`PUT    /api/v1/labs/answer/<int:qa_id>`

&cross; Delete answer a_id  
`DELETE /api/v1/labs/answer/<int:qa_id>`


### Teacher
&cross; create an experiment in the class class_id  
`POST   /api/v1/labs/exp/<int:class_id>`

&cross; update an experiment e_id  
`PUT    /api/v1/labs/exp/<int:e_id>`

&cross; delete an experiment e_d  
`DELETE  /api/v1/labs/exp/<int:e_id>`

&cross; create a question for experiment e_id  
`POST    /api/v1/labs/question/<int:e_id>`  

&cross; edit a question q_id  
`PUT     /api/v1/labs/question/<int:q_id>`  

&cross; delete a question q_id  
`DELETE  /api/v1/labs/question/<int:q_id>`  

&cross; add a testcase for question q_id  
`POST    /api/v1/labs/testcase/<int:q_id>`

&cross; edit testcase t_id  
`PUT     /api/v1/labs/testcase/<int:t_id>`

&cross; delete testcase t_id  
`DELETE  /api/v1/labs/testcase/<int:t_id>`