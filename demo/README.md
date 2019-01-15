Prerequisities for the demo:

* Docker installed
* Python installed

The demo contains two folders:

server - a node.js mock server hosting a "login" and "get user" APIs.

tests - python tests using the mock server as a backend

Running the mock backend:

docker-compose build
docker-compose up

Running pytest API tests:

in tests/api_pytest folder:

python -m pytest

Running locust performance tests:

Open browser http://192.168.99.100:8089 to use the Locust UI

Scaling the locust slaves:
docker-compose scale locust=<numofslaves>
