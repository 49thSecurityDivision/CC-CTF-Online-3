FROM python:3.9

WORKDIR /etc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir /etc/secrets
RUN echo "Flag{tr4v3rs4l_3xp3rt}" > /etc/secrets/flag.txt

EXPOSE 8091

CMD ["python", "main.py"]
