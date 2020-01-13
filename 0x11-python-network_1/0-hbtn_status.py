#!/usr/bin/python3
""" Fetch https://intranet.hbtn.io/status """

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()
print('Body response:\n\t- type: {}'.format(type(body)))
print('\t- content: {}'.format(body))
print('\t- utf8 content: {}'.format(body.decode('utf-8')))
