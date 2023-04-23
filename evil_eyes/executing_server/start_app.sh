#!/bin/sh

export FLASK_APP=server

flask run -h 0.0.0.0 -p 1337
