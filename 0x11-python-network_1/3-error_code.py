#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the body of the response in utf-8 managing urllib.error.HTTPError
exceptions
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as r:
            readed = r.read().decode('utf-8')
            print(readed)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
