#!/bin/sh
# Wait for PostgreSQL to be available
while ! pg_isready -h db -p 5432 -U postgres; do
  echo "Waiting for postgres..."
  sleep 2
done

# Run migrations and start the Django server
python manage.py migrate
python manage.py collectstatic --noinput
exec "$@"
