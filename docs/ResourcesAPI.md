# API Documentation


## Resources

- Get detailed data of resource r_id  
`GET    /api/v1/resources/res/<int:r_id>`

### Student
- List all resources (Student only)  
`GET    /api/v1/resources`

- List all resources in a semester sem (Student only)  
`GET    /api/v1/resources/sem/<int:sem>`

### Teacher
- create a resource in the class class_id  
`POST   /api/v1/resources/res/<int:class_id>`

    request data:
    ```js
    {
        res_name: String,  
        description: String,  
    }
    ``` 

    response data: 
    ```js
    {
        id: Number,
        res_name: String,
        description: String,
        created: String,
        modified: String,
    }
    ```

- update a resource r_id  
`PUT    /api/v1/resources/res/<int:r_id>`

    request data:
    ```js
    {
        res_name: String,
        description: String,
    }
    ```

    response data:
    ```js
    {
        id: Number,
        res_name: String,
        description: String,
        created: String,
        modified: String,
    }
    ```

- delete a resource r_d  
`DELETE  /api/v1/resources/res/<int:r_id>`  

    NOTE: deleting a resource also deletes its resource files


- create a resource file for resource r_id  
`POST    /api/v1/resources/file/<int:r_id>`  

- edit a resource file  
`PUT     /api/v1/resources/file/<int:rf_id>`  

- delete a resource file  
`DELETE  /api/v1/resources/file/<int:rf_id>`  



Future API:  
- list of resources in a class class_id  
`GET    /api/v1/resources/class/<int:class_id>`  