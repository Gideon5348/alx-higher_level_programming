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

    full_url = url + 'withemail=' + email
    response = requests.post(full_url)

    print("Your email is:", response.text)
