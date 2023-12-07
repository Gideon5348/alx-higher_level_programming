#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and
displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        request = urllib.request.Request(url, data=data, method='POST')

        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    else:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)
