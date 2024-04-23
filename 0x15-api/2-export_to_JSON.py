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

    name = json.loads(res.text)["username"]
    task = json.loads(res1.text)
    dump = {sys.argv[1]: []}
    for x in task:
        dump[sys.argv[1]].append({"task": x.get('title'),
                                  "completed": x.get('completed'),
                                  "username": name})
    file = open(f"{sys.argv[1]}.json", "w")
    json.dump(dump, file)
    file.close()
