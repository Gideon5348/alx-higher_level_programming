#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (for 200 status code)
curl -s -X GET -w "%{http_code}" "$1" -o /dev/null | { read -r status; [ "$status" -eq 200 ] && curl -s "$1" || echo ""; }
