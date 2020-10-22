#!/bin/sh
ps aux|grep mysch.py|grep -v grep|awk '{print $2}'|xargs kill -9
ps aux|grep app.py|grep -v grep|awk '{print $2}'|xargs kill -9
