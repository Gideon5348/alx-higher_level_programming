#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a GitHub repository
by a specific user
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Define the GitHub API endpoint for listing commits
    url = (
        f'https://api.github.com/repos/{owner_name}/'
        f'{repo_name}/commits'
    )

    # Set up the request headers
    headers = {'Accept': 'application/vnd.github.v3+json'}

    # Send GET request to GitHub API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the first 10 commits
        commits = response.json()[:10]

        # Print each commit in the specified format
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')

    else:
        # If there is an issue, print an error message
        print(f"Error: Unable to fetch commits. Status Code:
              {response.status_code}")
