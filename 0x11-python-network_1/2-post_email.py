#!/usr/bin/python3
"""Takes in a URL and an email,
sends a POST request to the URL with the email,
displays the body of the response decoded in uttf-8
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    val = {'email': argv[2]}
    content = urllib.parse.urlencode(val).encode('ascii')
    re = urllib.request.Request(argv[1], data=content, method='POST')
    with urllib.request.urlopen(re) as r:
        readed = r.read().decode('utf-8')
        print(readed)
