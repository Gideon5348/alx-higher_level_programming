#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response

file_content=$(cat "$2" 2>/dev/null)

if [[ -z "$file_content" ]]; then
    echo "Unable to read file: $2"
else
    curl -sX POST -H "Content-Type: application/json" -d "$file_content" "$1"
fi
