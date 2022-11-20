#!/bin/sh

# shellcheck disable=SC1035
#if [ "$DATABASE" = "postgres" ]
#then 
#    echo "Waiting for postgres..."
#
#    while != nc -z "$POSTGRESQLHOST" "$POSTGRESQLPORT"; do
#        sleep 0.1
#    done
#
#    echo "PostgresSQL started"
#fi
#
#python manage.py flush --no-input
#python manage.py migrate
#
#exec "$@"

# Before PostgreSQL can function correctly, the database cluster must be initialized:
initdb -D /var/lib/postgres/data

# internal start of server in order to allow set-up using psql-client
# does not listen on external TCP/IP and waits until start finishes
pg_ctl -D "/var/lib/postgres/data" -o "-c listen_addresses='5432'" -w start

# create a user or role
psql -d postgres -c "CREATE USER admin WITH PASSWORD 'erkerke2';" 

# create database 
psql -v ON_ERROR_STOP=1 -d postgres -c "CREATE DATABASE dockertest OWNER 'admin';"

# stop internal postgres server
pg_ctl -v ON_ERROR_STOP=1 -D "/var/lib/postgres/data" -m fast -w stop

exec "$@"
