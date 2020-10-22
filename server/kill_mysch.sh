#!/bin/sh
ps aux|grep mysch.py|grep -v grep|awk '{print $2}'|xargs kill -9
