#!/usr/bin/python3
"""
Takes in a string and sends a search request to the Star Wars API
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    result = requests.get('https://api.github.com/user',
                          auth=(argv[1], argv[2]))
    try:
        print(result.json()['id'])
    except KeyError:
        print("None")
