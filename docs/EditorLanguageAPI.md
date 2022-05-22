## Editor Language

- Get all languages  
`GET    /api/v1/languages`

    response:
    ```js
    {
        "id": Number,
        "language": String,
        "piston_lang": String,
        "editor_lang": String
    }
    ```

- Get language demo for language lang_id  
`GET    /api/v1/languages/<int:lang_id>`

    response:
    ```js
    {
        "demo_code": String
    }
    ```