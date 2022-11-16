#!/bin/sh

# shellcheck disable=SC1035
if [ "$DATABASE" = "postgres" ]
then 
    echo "Waiting for postgres..."

    while != nc -z "$POSTGRESQLHOST" "$POSTGRESQLPORT"; do
        sleep 0.1
    done

    echo "PostgresSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
