#!/usr/bin/env bash
set -o errexit

echo "=============================================="
echo " Starting Portfolio Build..."
echo "=============================================="

export DJANGO_SETTINGS_MODULE="portfolio.settings.production"

echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

echo "Running migrations..."
python manage.py migrate --noinput
echo "✓ Migrations done"

echo "Collecting static files..."
mkdir -p static
python manage.py collectstatic --noinput --clear
echo "✓ Static files collected"

echo "System check..."
python manage.py check --deploy
echo "✓ All systems ready"

echo "=============================================="
echo " Build complete!"
echo "=============================================="