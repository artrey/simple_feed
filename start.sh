#!/bin/bash

python3 manage.py migrate
python3 manage.py collectstatic --no-input

cp assets/favicon.ico static/

gunicorn simple_feed.wsgi -w 4 -t 600 -b 0.0.0.0:8000
