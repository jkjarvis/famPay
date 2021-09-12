FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY . /app