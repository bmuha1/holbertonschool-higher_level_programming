#!/usr/bin/python3
""" Fetch the value of the X-Request-ID variable found in the header """

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
