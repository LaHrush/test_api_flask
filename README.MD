Simple API CRUD
----------------------------------------------
Using::
- FLASK
- Marshmallow (serialization/deserialization library)
- SQLAlchemy
- Docker and Docker compose
- makefile to run application
    

****
    To run application used command : make

****
----------------------------------------------
    GET request
    Without id
    curl -i http://localhost:5000/ai-quotes/
----------------------------------------------
    POST request
    curl -i -H "Content-Type: application/json" -X POST -d '{"author":"Vadym", "quote":"Test API"}' http://localhost:5000/ai-quotes/
----------------------------------------------
    PUT request
    curl -i -H "Content-Type: application/json" -X PUT -d '{"author": "Nikola Tesla", "quote":"Be alone, that is the secret of invention; be alone, that is when ideas are born."}' http://localhost:5000/ai-quotes/1
----------------------------------------------
    DELETE request
    curl -X DELETE http://localhost:5000/ai-quotes/1