FROM ubuntu:20.04

RUN apt update -y
RUN apt upgrade -y
RUN apt install firejail -y
RUN apt install python3 python3-pip -y

COPY ./server.py /app/server.py
COPY ./start_app.sh /app/start_app.sh
COPY ./flag/ /app/flag/
COPY ./templates/ /app/templates/
COPY ./static/ /app/static/
COPY ./uploads/ /app/uploads/
COPY ./MD5 ./app/MD5
COPY ./output.txt /app/output.txt
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT /app/start_app.sh
