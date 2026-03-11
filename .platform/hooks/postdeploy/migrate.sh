#!/bin/bash

# Stop script if any command fails
set -e

echo "========================================"
echo "Starting database migration..."
echo "========================================"

# Navigate to application directory
cd /var/app/current

echo "Current directory:"
pwd

# Activate virtual environment used by Elastic Beanstalk
echo "Activating Python virtual environment..."
source /var/app/venv/*/bin/activate

# Set Flask environment variables
export FLASK_APP=application.py
export FLASK_ENV=production

echo "Running Flask database migration..."

# Run migrations
flask db upgrade

echo "========================================"
echo "Database migration completed successfully"
echo "========================================"