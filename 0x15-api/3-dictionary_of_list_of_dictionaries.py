#!/usr/bin/python3
"""Requests check status."""
import json
import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com"
    res = requests.get(url + "/users")
    res1 = requests.get(url + "/todos")
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
        exit(1)

    name = json.loads(res.text)
    task = json.loads(res1.text)
    dump = {}
    for x in task:
        for i in name:
            if i["id"] == x.get("userId"):
                namex = i["username"]
        try:
            dump[x.get("userId")].append({"username": namex,
                                          "completed": x.get('completed'),
                                          "task": x.get('title')})
        except KeyError:
            dump[x.get("userId")] = [{"username": namex,
                                      "completed": x.get('completed'),
                                      "task": x.get('title')}]
    file = open("todo_all_employees.json", "w")
    json.dump(dump, file)
    file.close()
