#!/bin/bash

echo "Running database migrations..."

cd /var/app/current

source /var/app/venv/*/bin/activate

flask db upgrade

echo "Migration completed"