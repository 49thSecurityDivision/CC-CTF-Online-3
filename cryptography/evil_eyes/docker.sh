#!/bin/sh

docker build -t evileyes:1.0 . && \
docker run --dns=1.1.1.1 -t --name evileyes -d --rm --network host evileyes:1.0
