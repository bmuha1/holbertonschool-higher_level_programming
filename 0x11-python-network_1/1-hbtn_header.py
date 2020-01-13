#!/usr/bin/python3
""" Fetch the value of the X-Request-ID variable found in the header """

if __name__ == '__main__':
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        xreqid = response.getheader('X-Request-ID')
    print(xreqid)
