#!/usr/bin/python3
"""Get top from reddit api."""
from requests import get


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Use the Reddit api."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/97.0.4692.99 Safari/537.36"}
    res = get(url, headers=h,
              params={"count": count, "after": after}, allow_redirects=False)

    if res.status_code == 200:
        try:
            hot = hot_list + [child.get("data").get("title")
                              for child in res.json().get("data")
                              .get("children")]
            info = res.json()
            if not info.get("data").get("after"):
                return hot
            return recurse(subreddit, hot, info.get("data").get("count"),
                           info.get("data").get("after"))
        except Exception as e:
            return None
    else:
        return None
