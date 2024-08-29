#Write a function that validates a URL string. Handle the ValueError by raising a custom exception if the URL format is invalid.Write a function that removes an element at a specified index from a list. Handle the IndexError by raising a custom exception if the index is out of range.

import re

def validate_url(url):
    if not re.match(r'^(http://|https://)', url):
        raise ValueError("Invalid URL format. URL must start with 'http://' or 'https://'.")
    return True
try:
    validate_url("https://example.com")
    print("URL is valid.")
except ValueError as e:
    print(e)

try:
    validate_url("ftp://example.com")
except ValueError as e:
    print(e)
