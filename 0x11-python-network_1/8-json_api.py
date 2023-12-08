#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter parameter
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL and data parameters
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    # Send the POST request
    response = requests.post(url, data=data)

    try:
        # Try to parse the JSON response
        json_response = response.json()

        # Check if the JSON is not empty
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
