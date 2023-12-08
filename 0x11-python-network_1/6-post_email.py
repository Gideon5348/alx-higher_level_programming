#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Ensure there is a forward slash between the URL and email
    if not url.endswith('/'):
        url += '/'

    full_url = url + 'post_email'
    data = {'email': email}

    response = requests.post(full_url, data=data)

    # Check if the response is a 404 error
    if response.status_code == 404:
        print("Error 404: The requested URL was not found.")
    else:
        print(response.text)
