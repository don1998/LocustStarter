# Locust Starter
A starter project for a simple load-testing python framework built using locust.io.

## Links
Docker Hub Repository: [Locust Starter Image] (https://hub.docker.com/repository/docker/dscotland98/locust_starter)

## Getting Started

### Requirements
1. [Docker Engine](https://docs.docker.com/engine/install/)

### Usage

Getting the image:

`docker pull dscotland98/locust_starter:latest`

Executing the image:

`docker run -e TARGET_URL=<endpoint_to_be_tested> -e LOCUSTFILE_PATH=/locustfiles/api_load_test.py -p 8089:8089  locust_starter`

Navigate to and start the test:

`http://localhost:8089/`
