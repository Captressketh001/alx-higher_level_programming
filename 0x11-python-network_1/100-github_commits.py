#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()[:10]
        for i in data:
            sha = i['sha']
            author = i['commit']['author']['name']
            print("{}: {}".format(sha, author))
    else:
        print("None")
