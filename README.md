# Needs Assessment Toolbox

Needs Assessment Toolbox website for UNHCR

## Installation

### Requirements

* [Docker (1.13.0+)](https://docs.docker.com/engine/installation/)
* [docker-compose](https://github.com/docker/compose/releases)

### Build docker image

```
$ docker-compose build
```

### Running locally

```
$ docker-compose up
```

### Running on production

Copy *production.envsample* to *production.env* and modify the environment settings to match postgres database settings.

Make sure to also modify `ALLOWED_HOST`.

The production configuration for docker-compose is in *production.yml*.

Some of the usefull `docker-compose` commands

```
$ docker-compose -f production.yml pull     # Pull images from docker hub instead of building
$ docker-compose -f production.yml build    # Build images from docker hub instead of pulling
$ docker-compose -f production.yml push     # Push images to docker hub

$ docker-compose -f production.yml up       # Start container [Will build images if not exists]

$ docker-compose -f production.yml down     # To shut down already running docker image
$ docker-compose -f production.yml down -v  # [`Alert`] To shut down already running docker image plus remove persistent volumes
```
