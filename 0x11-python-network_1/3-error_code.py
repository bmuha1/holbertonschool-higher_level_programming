#!/usr/bin/python3
"""
Send a POST request to the passed URL and display the body of the response,
managing HTTPError exceptions
"""

if __name__ == '__main__':
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
        print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
