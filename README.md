# Locust Starter
A starter project for a simple load-testing python framework built using locust.io.

## Links
Docker Hub Repository: [Locust Starter Image] (https://hub.docker.com/repository/docker/dscotland98/locust_starter)

## Getting Started

### Requirements
1. [Docker Engine](https://docs.docker.com/engine/install/)

### Usage

1. Getting the image:

`docker pull dscotland98/locust_starter:latest`

2. Executing the image:

`docker run -e TARGET_URL=<endpoint_to_be_tested> -e LOCUSTFILE_PATH=/locustfiles/api_load_test.py -p 8089:8089  locust_starter`

3. Navigate to `http://localhost:8089/` and begin the test:
