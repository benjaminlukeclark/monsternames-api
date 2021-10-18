#!/bin/sh
python3 database/setup.py
python3 -m flask run --host=0.0.0.0