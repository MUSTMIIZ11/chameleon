# syntax=docker/dockerfile:1
FROM python:3.7-alpine
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install PillowENV PYTHONUNBUFFERED=1
WORKDIR "/code"
COPY requirements /code/
RUN pip install -r requirements
COPY . /code/
ENV DJANGO_ENV=devlopment
CMD python manage.py runserver 0.0.0.0:9090
