#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'
    repo = argv[1]
    owner = argv[2]

    payload = {'owner': owner, 'repo': repo}
    res = requests.get(url, params=payload)
    if res.status_code == 200:
        data = res.json()[:10]
        print(data)
    else:
        print("None")
