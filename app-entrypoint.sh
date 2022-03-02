#!/bin/sh
set -e

echo "Waiting for Postgres (2 seconds)..."

#
alembic current

sleep 2
streamlit run app/app.py

