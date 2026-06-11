#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

echo "--> Applying database migrations..."
python manage.py migrate --noinput

echo "--> Creating superuser if it doesn't exist..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@email.com', 'admin123')
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
EOF

echo "--> Starting Gunicorn..."
# 'exec' ensures Gunicorn becomes PID 1, receiving OS signals perfectly
exec gunicorn projetoweb.wsgi:application --bind 0.0.0.0:8000 --workers 2
