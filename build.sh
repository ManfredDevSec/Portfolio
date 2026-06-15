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

echo "Verifying staticfiles output..."
FILE_COUNT=$(find staticfiles -type f | wc -l)
echo "  Total files in staticfiles/: $FILE_COUNT"
if [ "$FILE_COUNT" -lt 1 ]; then
    echo "ERROR: staticfiles/ is empty — collectstatic produced nothing" >&2
    exit 1
fi
ls -1 staticfiles/

echo "System check..."
python manage.py check --deploy
echo "✓ All systems ready"

echo "=============================================="
echo " Build complete!"
echo "=============================================="