#!/bin/sh

docker build -t off-the-land:latest .
docker run -t --name off-the-land -p880:80 -p 8443:443 -p20000-20500:20000-20500 -d --rm off-the-land:latest
