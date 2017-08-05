#!/bin/bash

. /venv/bin/activate
python manage.py collectstatic
python manage.py migrate
uwsgi --socket natoolbox.sock --module natoolbox.wsgi --chmod-socket=666 -H /venv

