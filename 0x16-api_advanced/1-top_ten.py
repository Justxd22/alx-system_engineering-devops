#!/usr/bin/python3
"""Get top 10 from reddit api."""
from requests import get


def top_ten(subreddit):
    """Use the Reddit api."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/97.0.4692.99 Safari/537.36"}
    res = get(url, headers=h)

    if res.status_code == 200:
        try:
            top = res.json()
            for x in top["data"]["children"]:
                print(x["data"]["title"])
        except Exception as e:
            return None
    else:
        return None
