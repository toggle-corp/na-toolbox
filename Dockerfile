FROM python:3.6-alpine

MAINTAINER togglecorp info@togglecorp.com

RUN apk update \
    && apk add --no-cache \
        postgresql-libs \
        bash \
    && apk add --virtual \
        .build-deps \
        gcc \
        musl-dev \
        libc-dev \
		linux-headers \
        postgresql-dev \
    && python3 -m pip install uwsgi psycopg2 --no-cache-dir \
    && apk --purge del .build-deps

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
