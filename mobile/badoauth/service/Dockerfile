FROM python:3.9-slim


RUN apt-get update && \
      apt-get install -y python3 python3-pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "/app/main.py"]
