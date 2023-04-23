#!/bin/sh

socat -dd tcp-listen:8002,reuseaddr,fork EXEC:"/trash"
