#!/bin/sh

# Verify postgres is healthy, then apply migrations.
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started."
fi

python manage.py collectstatic --no-input
python manage.py migrate --no-input

exec "$@"