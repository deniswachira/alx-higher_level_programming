#!/usr/bin/python3
"""
Takes in a URL, sends a requestt to the URL and displays the value of
the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    val = {'email': argv[2]}
    re = requests.post(url=argv[1], data=val)
    t = re.text
    print(t)
