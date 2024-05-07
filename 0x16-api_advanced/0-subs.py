#!/usr/bin/python3
# get subs
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """subs"""
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/97.0.4692.99 Safari/537.36"}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=h).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
