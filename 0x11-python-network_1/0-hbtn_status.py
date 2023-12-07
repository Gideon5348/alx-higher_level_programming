#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
