#! /usr/bin/env bash

# Let the DB start
python ./initial_data.py

# Start Application
python -m uvicorn main:app
