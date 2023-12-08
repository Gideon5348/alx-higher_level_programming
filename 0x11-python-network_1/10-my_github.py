#!/usr/bin/python3
"""
Uses the GitHub API to display the user id
"""

import requests
import sys

if __name__ == "__main__":
    # Get GitHub username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the GitHub API endpoint for the authenticated user
    url = 'https://api.github.com/user'

    # Set up Basic Authentication with the provided username
    # and personal access token
    auth = (username, password)

    # Send GET request to GitHub API
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()

        # Display the user id
        print(user_data['id'])
    else:
        # If authentication fails or other issues, print None
        print(None)
