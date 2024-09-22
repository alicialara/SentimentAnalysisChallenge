#!/bin/bash

# Build and start the services defined in the docker-compose.yml file with no cache
docker-compose build --no-cache
docker-compose up
