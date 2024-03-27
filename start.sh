#!/bin/sh

until aerich migrate && aerich update
do
    echo "Waiting for db to be ready..."
    sleep 10
done
until uvicorn main:app --reload --host 0.0.0.0 --port 8000
do
    echo "Waiting for starting the application..."
    sleep 10
done
python3 load_data.py
