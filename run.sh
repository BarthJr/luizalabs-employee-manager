#!/bin/bash
pipenv sync -d
echo 'Setting the instance'
cp contrib/env-sample .env
echo 'Migrating the database'
python manage.py migrate --no-input
echo 'Creating superuser'
echo "from django.contrib.auth.models import User; User.objects.create_superuser('luiza.labs', 'luiza.labs@luizalabs.com', 'olhaseeenha')" | python manage.py shell
echo 'Running the tests'
pipenv run pytest
echo 'Starting the application'
python manage.py runserver
