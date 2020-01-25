#!/bin/bash

set -e

cd /usr/src/app/backend

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# when create a new script file make sure your script file is executable before copy all files with,
# chmod +x your/executable/file.sh
