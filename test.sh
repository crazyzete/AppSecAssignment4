#!/bin/bash
flask run &
sleep 10s
python curltest.py
kill -9 $(pgrep flask)
