# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements
COPY . /code/
RUN cd code && export DJANGO_ENV=devlopment && python manage.py runserver 8080
