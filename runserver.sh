#!/bin/sh
#python manage.py createsuperuser --noinput --username alchercaadmin --email alcher@gmail.com
python manage.py migrate
# python manage.py createsuperuser --noinput --firstname admin --email admin@admin.com
gunicorn testdb.wsgi:application --bind 0.0.0.0:80 --log-level=debug --timeout 180  --workers 4
