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

# Clear database and run migrate each time the container starts up.
# Can be commented out and run manually when necessary.
# To migrate manually, run this after the container is up:
#  docker-compose exec web python manage.py flush --no-input
#  docker-compose exec web python manage.py migrate
python manage.py flush --no-input
python manage.py migrate

exec "$@"