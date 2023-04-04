#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.read()

    print(html)
