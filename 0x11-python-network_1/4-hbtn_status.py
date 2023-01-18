#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status using requests
"""
if __name__ == "__main__":
    import requests
    r = requests.get('https://intranet.hbtn.io/status', auth=('user', 'pass'))
    print("Body response:")
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
