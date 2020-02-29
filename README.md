## Coding Test
The purpose of this coding test is to evaluate your software development skills with self-contained small projects.

We expect you to submit working source code as a git repository with a README explaining how to run both the tests and the actual program. Take into account that you ​must use ​Python 3​ for this exercise.

Your submission is going to be assessed in the following dimensions:
* Quality of the design and tradeoffs taken
* Clarity of the code (to what extent is self-explanatory and documented when not)
* Testing practices
* Algorithmic choices
* Common good practices
* Easiness to run the service (Containerization)

## Exercise: ​developers connected API
In this exercise, you will have to create a REST API which will return whether two “developers”
are fully connected or not. Given a pair of developer handles they are considered connected if:
* They follow each other on Twitter.
* They have at least a Github organization in common.

Assume that people having the same handle both in Twitter and Github are actually the same person.

## Real-time Endpoint
An example of a request to this endpoint for the handles @dev1 and @dev2 would be like:
```shell script
GET /connected/realtime/dev1/dev2
```
We expect the endpoint to return if the developers are connected and what GitHub organizations they have in common. The response should be in JSON format with the following structure:
* Case they are not connected:
```json
{
  "connected" : false
}
```
* Case they are connected:
```json
{
  "connected" : true,
  "organisations": ["org1", "org2", "org3"]
}
```
In case there are some errors the API should respond with a JSON describing the issue/s, for instance in case one or both handles does not exist in any of the services we should return a JSON like:
```json
{
  "errors": [
    "dev1 is no a valid user in github",
    "dev1 is no a valid user in twitter",
    "dev2 is no a valid user in twitter"
  ]
}
```

## Register Endpoint
Besides, we are interested in the different statuses a pair of developers had in previous invocations of the real-time endpoint:

This endpoint should be invoked with:
```
GET /connected/register/dev1/dev2
```
And it should return all the related information from previous requests to the real-time endpoint.

The response should be a list of found records in JSON format (or an empty list if no records are in the database). As in this example:
```json
[
  {
    "registered_at" : "2019-09-13T09:30:00Z",
    "connected" : false
  },
  {
    "registered_at" : "2019-09-15T10:30:00Z",
    "connected" : true,
    "organisations": ["org1", "org2", "org3"]
  },
  {
    "registered_at" : "2019-09-27T12:34:00Z",
    "connected" : true,
    "organisations": ["org1", "org2", "org3", "org4"]
  }
]
```

We expect the implementation to query the official ​Twitter​ and ​Github​ APIs and it is OK to use the existing client libraries for your target programming language.

## Recommendations
Please if you have any doubt don’t hesitate to get in contact with us, we will happily try to resolve/clarify all your questions.

Choose the tools that you prefer or consider the best for this task, here at jobandtalent we happily use Flask, SqlAlchemy, Alembic, Docker and many others, but feel free to use your favourites frameworks/tools.


## Commands
Before to run, you need to add a file called *secrets.py* with the next secrets keys:
* TWITTER_API_KEY
* TWITTER_API_SECRET_KEY
* TWITTER_ACCESS_TOKEN
* TWITTER_ACCESS_TOKEN_SECRET

* Run:
```shell script
make run
```

Check the API with http://127.0.0.1:8000/_health

* Tests:
```shell script
make tests
```

* Stop:
```shell script
make stop
```

* Delete:
```shell script
make rm
```

## Documentation

http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

## Considerations
* Using Docker for scalability.
* API created with [FastAPI](https://fastapi.tiangolo.com), it is a new microframework for me, and I rescue it
 from my TODO list, I think the challenge is a good moment to learn it.
    * OpenAPI documentation, auto-generated.
* PyTest and TestClient for easy e2e tests.
* Check PEP8 with pycodestyle with tests.

## Future task
- Twitter API: to improve the connections.
- Twitter API: manage the error: rate limit.
