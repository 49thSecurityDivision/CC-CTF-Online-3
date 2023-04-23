FROM ubuntu:20.04

RUN apt update -y
RUN apt upgrade -y
RUN apt install socat -y

COPY ./trash /trash
COPY ./script.sh /script.sh
COPY ./flag.txt /flag.txt

ENTRYPOINT /script.sh
