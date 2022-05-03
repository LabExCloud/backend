## Class

use request header:  
```http
Authorization: "Token <token>"
```

- list all classes a user has  
`GET    /api/v1/classes`

- view a class c_id  
`GET    /api/v1/class/<int:c_id>`