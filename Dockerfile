# syntax=docker/dockerfile:1
FROM python:3.7-alpine
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple && pip config set install.trusted-host mirrors.aliyun.com
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
WORKDIR "/code"
COPY requirements /code/
RUN pip install -r requirements
COPY . /code/
ENV DJANGO_ENV=devlopment
CMD python manage.py runserver 0.0.0.0:9090
