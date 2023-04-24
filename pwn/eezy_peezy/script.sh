#!/bin/sh

socat tcp-listen:8002,reuseaddr,fork EXEC:"/trash"
