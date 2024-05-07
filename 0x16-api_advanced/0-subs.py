#!/usr/bin/python3
"""Get user counts from reddit api."""
from requests import get
import sys


def number_of_subscribers(subreddit):
    """Use the Reddit api."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/97.0.4692.99 Safari/537.36"}
    res = get(url, headers=h, allow_redirects=False)

    if res.status_code == 200:
        try:
            users = res.json()
            users = users["data"]["subscribers"]
            return users
        except Exception as e:
            return 0
    else:
        return 0

if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
