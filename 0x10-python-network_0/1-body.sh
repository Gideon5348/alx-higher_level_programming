#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (for 200 status code)
curl -sL "$1"
