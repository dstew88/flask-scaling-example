# Simple Flask Scaling Example

Simple example of scaling a Flask application. Idea ported from an equivalent
Node.js/Express.js example [here](https://github.com/dstew88/node-express-scaling-example).

## Description

The web app asks the user to make either a blocking or non-blocking API request:
`http://localhost:8080/api/blocking`
`http://localhost:8080/api/non-blocking`

**NOTE: since this is a port of a Node.js example, the concept of "blocking" is
different here. the Flask app is deployed with gunicorn, so the response from
the server will be delayed for the `blocking` request, but it will not
necessarily block other client requests.**

The aim is to demonstrate a number of things:

* An example of a CPU intensive operation in Flask and its consequences for the response time;
* A solution to the above via a Celery worker process;
* A scalable deployment method using Docker Compose in order to instantiate:
  * Multiple instances of the `flask_server` Flask application deployed with gunicorn;
  * Redis;
  * A background Celery worker process;
  * An Nginx reverse-proxy acting as a load-balancer for the `flask_server` instances;
* Flask application project structure for `flask_server` application.

## Getting Started

To deploy, simply run:
```
docker-compose up --scale flask-server-instance=N
```
where `N` is the number of `flask_server` instances to deploy.

Navigate to `http://localhost:8080/` and select which API call to make.

### N = 1

When `N = 1`, there is only a single server instance, so a call to `http://localhost:8080/api/blocking`
will have a delayed response.
**It will not block the main server thread so further navigations to `http://localhost:8080/` and other API requests will be possible.**

### N > 1

When `N > 1`, there are multiple server instances, and API requests are amongst them via
the Nginx load-blanacer. Navigations to `http://localhost:8080/` and other
API requests may be handled depending on their routing by the load-balancer.

Each server instance will log that it has been hit with an API request, and this is visible in the log outputs
for each instance, demonstrating the load-balancer in effect.
