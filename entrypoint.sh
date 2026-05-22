#!/usr/bin/env bash
set -e

# Simple helper to wait for Postgres to be ready
host="$POSTGRES_HOST"
port=${POSTGRES_PORT:-5432}

until nc -z "$host" "$port"; do
  echo "Waiting for Postgres at $host:$port..."
  sleep 1
done

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Collect static files
echo "Collect static files"
mkdir -p /home/appuser/projeto/staticfiles
chown -R appuser:appuser /home/appuser/projeto/staticfiles
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn"
if [ "$(id -u)" -eq 0 ]; then
  exec su appuser -c 'gunicorn app.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level info \
    --access-logfile - \
    --error-logfile -'
else
  exec gunicorn app.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level info \
    --access-logfile - \
    --error-logfile -
fi
