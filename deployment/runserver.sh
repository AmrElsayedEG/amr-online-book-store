#!/bin/sh
gunicorn book_store.wsgi:application --bind=0.0.0.0:8000 --timeout 300