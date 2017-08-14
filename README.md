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

For Detach mode

```
$ docker-compose -f production.yml up -d     # to start container in detach mode
$ docker-compose -f production.yml logs -f   # to look at logs
$ docker-compose -f production.yml stop      # Stop the containers
```

## Without the docker

Create Virtualenv and install dependency

```bash
pip3 install virtualenv
virtualenv -p python3 {parent_directory_of_code_location}/venv
source {parent_directory_of_code_location}/venv/bin/activate
cd {your_code_location}
pip3 install requirements.txt
cp production.envsample production.env
vim production.env # modify the env parameters
```

Install nginx Uwsgi

```bash
sudo apt update
sudo apt install -f python3-dev uwsgi nginx uwsgi-plugin-python3 vim
```

Add nginx config `/etc/nginx/sites-enabled/natoolbox.conf`

Nginx Config
```nginx
upstream django {
    server unix://{your_code_location}/natoolbox.sock;
}

server {
    listen 80;
    server_name im.unhcr.org;
    charset utf-8;

    client_max_body_size 75M;

    location /media {
        alias {your_code_location}/media;
    }

    location /static {
        alias {your_code_location}/static;
    }

    location / {
        uwsgi_pass django;
        include /etc/nginx/uwsgi_params;
    }
}
```

Add uwsgi config

```bash
sudo mkdir -p /etc/uwsgi/sites/
sudo vim /etc/uwsgi/sites/natoolbox.ini
```

UWSGI CONFIG
```uwsgi
[uwsgi]

chdir = {ycour_code_location}
module = natoolbox.wsgi
home =  {parent_directory_of_code_location}/venv/lib/python

master = true
processes = 10
socket = {ycour_code_location}/natoolbox.sock
chmod = 666
plugins = python34

vacuum = true
http-timeout = 300
virtualenv = {parent_directory_of_code_location}/venv/

req-logger = file:/var/log/uwsgi/access.log
logger = file:/var/log/uwsgi/error.log
log-maxsize = 10240
```

Create a Init file for uWSGI

```bash
sudo vim /etc/init/uwsgi.conf
```

Uwsgi Init config
```

description "uWSGI application server in Emperor mode"

start on runlevel [2345]
stop on runlevel [!2345]

env LANG="en_US.utf8"
env LC_ALL="en_US.UTF-8"
env LC_LANG="en_US.UTF-8"
exec /usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
```

Restart the nginx and uwsgi server
```
sudo service uwsgi restart
sudo service nginx restart
```
