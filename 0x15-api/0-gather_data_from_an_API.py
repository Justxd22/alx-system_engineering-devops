#!/usr/bin/python3
"""Requests check status."""
import json
import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    res = requests.get(url)
    res1 = requests.get(url + "/todos")
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
        exit(1)
    name = json.loads(res.text)["name"]
    task = json.loads(res1.text)
    lentasks = len(task)
    done = []
    for i in task:
        if i["completed"]:
            done.append(i)
    print(f"Employee {name} is done with tasks({len(done)}/{lentasks}):")
    for i in done:
        t = i["title"]
        print(f"         {t}")
