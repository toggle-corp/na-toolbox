#!/bin/bash

python manage.py collectstatic --no-input
python manage.py migrate --no-input
uwsgi --http 0.0.0.0:80 --module natoolbox.wsgi --chmod-socket=666
