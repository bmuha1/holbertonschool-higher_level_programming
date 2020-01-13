#!/usr/bin/python3
"""
Send a POST request to http://0.0.0.0:5000/search_user with letter as a
parameter
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 1:
        q = ''
    else:
        q = argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    data = r.json()
    if r.headers.get('content-type') != 'application/json':
        print('Not a valid JSON')
    elif len(data) == 0:
        print('No result')
    else:
        print('[{}] {}'.format(data['id'], data['name']))
