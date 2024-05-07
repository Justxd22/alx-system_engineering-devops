#!/usr/bin/python3
"""Count words in hot posts of a subreddit."""
from requests import get


def count_words(subreddit, word_list, after=None, counts={}):
    """Use the Reddit api."""
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/97.0.4692.99 Safari/537.36"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    res = get(url, headers=h, params=params, allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json()
    children = data["data"]["children"]

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sort = sorted(counts.items(),
                      key=lambda x: (-x[1], x[0].lower()))
        for word, count in sort:
            print(f"{word.lower()}: {count}")
