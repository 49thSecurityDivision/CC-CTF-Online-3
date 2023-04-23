#!/bin/sh

docker build -t trash:1.0 .
docker run -t --name trash -d --rm --network host trash:1.0
