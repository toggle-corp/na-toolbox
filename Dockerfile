FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install -y \
        python3 \
        python3-dev \
        python3-setuptools \
        python3-pip \
        ruby-sass

RUN pip3 install uwsgi


RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install virtualenv

RUN virtualenv /venv
RUN . /venv/bin/activate && pip install -r requirements.txt

COPY . /code/
