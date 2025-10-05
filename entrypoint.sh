#!/bin/bash
set -e

# Run migrations
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
# Check if the superuser already exists
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  echo "Checking if superuser exists..."
  if ! pipenv run python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists())" | grep -q "True"; then
    echo "Creating superuser..."
    pipenv run python manage.py createsuperuser --no-input
  else
    echo "Superuser already exists."
  fi
fi

# Start the server
exec pipenv run python manage.py runserver 0.0.0.0:8000
