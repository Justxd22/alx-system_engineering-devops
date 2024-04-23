#!/usr/bin/python3
"""Requests check status."""
import requests
import sys
import json
import csv

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    res = requests.get(url)
    res1 = requests.get(url + "/todos")
    print(url + "/todo")
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
        exit(1)

    name = json.loads(res.text)["name"]
    task = json.loads(res1.text)

    file = open(f"{sys.argv[1]}.csv", "w")
    pointer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for x in task:
        line = [x.get('userId'), name,
                x.get('completed'), x.get('title')]
        pointer.writerow(line)
    file.close()
