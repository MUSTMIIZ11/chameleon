# syntax=docker/dockerfile:1
FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR "/code"
COPY requirements /code/
RUN pip install -r requirements
COPY . /code/
ENV DJANGO_ENV=devlopment
CMD python manage.py runserver 0.0.0.0:9090
