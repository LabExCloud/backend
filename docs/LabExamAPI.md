## Lab Exam

&cross; Get all exams in lab c_id  
`GET    /api/v1/labexams/exam/<int:c_id>`

&cross; Get detail of lab exam e_id  
`GET    /api/v1/labexams/exam/<int:e_id>`

&cross; Get detail of question q_id  
`GET    /api/v1/labexams/question/<int:q_id>`

### Student
&cross; List all lab exams in current semester  
`GET    /api/v1/labs`

&cross; List all lab exams in a semester sem  
`GET    /api/v1/labs/sem/<int:sem>`

&cross; Add answer for the question q_id  
`POST   /api/v1/labexams/answer/<int:q_id>`


### Teacher
&cross; create a lab exam in the class class_id  
`POST   /api/v1/labexams/exam/t:class_id>`

&cross; update a lab exam e_id  
`PUT    /api/v1/labexams/exam/t:e_id>`

&cross; delete a lab exam e_d  
`DELETE  /api/v1/labexams/exam/t:e_id>`

&cross; create a question for lab exam e_id  
`POST    /api/v1/labexams/question/<int:e_id>`  

&cross; edit a question q_id  
`PUT     /api/v1/labexams/question/<int:q_id>`  

&cross; delete a question q_id  
`DELETE  /api/v1/labexams/question/<int:q_id>`  

&cross; add a testcase for question q_id  
`POST    /api/v1/labexams/testcase/<int:q_id>`

&cross; edit testcase t_id  
`PUT     /api/v1/labexams/testcase/<int:t_id>`

&cross; delete testcase t_id  
`DELETE  /api/v1/labexams/testcase/<int:t_id>`