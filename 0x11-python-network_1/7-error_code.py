#!/usr/bin/python3
"""
Takes in a URL, sends a requestt to the URL and displays the value of
the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    status = requests.get(argv[1]).status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(requests.get(argv[1]).text)
