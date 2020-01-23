FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /usr/src/app/backend/

WORKDIR /usr/src/app/backend/


COPY . /usr/src/app/backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
