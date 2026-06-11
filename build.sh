#!/usr/bin/env bash
# build.sh

set -o errexit

echo "=============================================="
echo "Starting Portfolio App Build Process..."
echo "=============================================="

export DJANGO_SETTINGS_MODULE="portfolio.settings.production"

echo "=============================================="
echo "Checking if Django is available..."
echo "=============================================="
if python -c "import django" 2>/dev/null; then
    echo "✓ Django is available - running setup commands"

    echo "Running database migrations..."
    python manage.py migrate --noinput
    echo "✓ Database migrations completed"

    echo "Collecting static files..."
    mkdir -p static
    #python manage.py collectstatic --noinput --clear
    python manage.py collectstatic --noinput --clear -v 2
    echo "✓ Static files collected"

    echo "Final system check..."
    python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.production')
import django
django.setup()
from django.core.wsgi import get_wsgi_application
from django.db import connection

application = get_wsgi_application()
with connection.cursor() as cursor:
    cursor.execute('SELECT 1')
print('✓ All systems ready!')
    "
else
    echo "  Django not available yet - skipping Django operations"
    echo "  Run migrations and setup commands manually after deployment"
fi

echo "=============================================="
echo " Build process completed!"
echo "=============================================="