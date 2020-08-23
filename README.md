# recyclabox-api

## Overview
The recyclabox web API consists of a set of callable API endpoints. To perform an action using the recyclabox API, you need to send a request to its endpoint specifying a method and some arguments, and you will subsequently receive a response.

## recyclabox API is entirely HTTP-based
Methods to retrieve data from the recyclabox API require a **GET** request. Methods that submit data require a **POST** and methods that change data require a **PATCH**. Any DELETE requests are not currently accepted for methods that destroy data. API Methods that require a particular HTTP method will return an error if you do not make your request with the correct method.

## Endpoints
All API methods follow the following format: **http://127.0.0.1:8000/api/{method_endpoint}**

Example endpoint for Single-Product look-up method: **http://127.0.0.1:8000/api/product-details/1**

```
Response Codes
Response Codes
200: Success
400: Bad request
401: Unauthorized
404: Cannot be found
405: Method not allowed
422: Unprocessable Entity 
50X: Server Error
```
