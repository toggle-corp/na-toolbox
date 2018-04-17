FROM ubuntu:16.04

# Clean apt
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/lib/apt/lists/partial/* && \
    rm -rf /var/cache/apt/*

RUN apt-get update -y && \
    apt-get install -y \
        # Basic Packages
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
