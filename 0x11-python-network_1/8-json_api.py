#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to 8-json_api.py
with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 1:
        dic = {'q': ""}
    else:
        dic = {'q': argv[1]}

    response = requests.post(url='http://0.0.0.0:5000/search_user', data=dic)
    d = response.json()
    if response.headers.get('content-type') != 'application/json':
        print('Not a valid JSON')
    elif d == {}:
        print('No result')
    else:
        print('[{}] {}'.format(d['id'], d['name']))
