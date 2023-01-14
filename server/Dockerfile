FROM python:3.8.4-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python3", "server.py"]
