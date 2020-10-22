#!/bin/sh
#nohup gunicorn -w 10 -b 0.0.0.0:5000 app:app /dev/null 2>&1 &
nohup python app.py /dev/null 2>&1 &
