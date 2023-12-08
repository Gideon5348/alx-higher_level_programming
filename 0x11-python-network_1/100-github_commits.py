#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests


def list_commits(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")

    else:
        print(f"Error: Unable to fetch commits. Status Code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo_owner = sys.argv[1]
        repo_name = sys.argv[2]
        list_commits(repo_owner, repo_name)
    else:
        print("Usage: ./script.py <repository_owner> <repository_name>")
