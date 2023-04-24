#!/bin/sh

docker build -t mentor:latest .
docker run -d -p 5252:80 -p 61337:61337 --name mentor mentor
