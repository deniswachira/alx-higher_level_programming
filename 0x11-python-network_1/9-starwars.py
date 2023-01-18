#!/usr/bin/python3
"""
Takes in a string and sends a search request to the Star Wars API
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    d = r.json()
    print("Number of results: {}".format(d['count']))
    for i in d['results']:
        print(i['name'])
