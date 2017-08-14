#!/bin/bash

. /venv/bin/activate
python manage.py collectstatic --no-input
python manage.py migrate --no-input
uwsgi --socket /socket/natoolbox.sock --module natoolbox.wsgi --chmod-socket=666 -H /venv

