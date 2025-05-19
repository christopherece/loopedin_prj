#!/bin/sh

set -e

# Hardcoded admin credentials
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=adminpass

echo "Using hardcoded admin credentials: $DJANGO_SUPERUSER_USERNAME / $DJANGO_SUPERUSER_EMAIL"

# Apply makemigrations
echo "Running makemigrations..."
python manage.py makemigrations

# Apply migrations
echo "Running migrate..."
python manage.py migrate

# Create superuser if not exists
echo "Checking/Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
username = "$DJANGO_SUPERUSER_USERNAME"
email = "$DJANGO_SUPERUSER_EMAIL"
password = "$DJANGO_SUPERUSER_PASSWORD"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")
EOF

# Start the main container command
exec "$@"
