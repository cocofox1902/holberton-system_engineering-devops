#!/usr/bin/python3
""" 2 - export to JSON """
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    user_url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(id))
    todo_url = (requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    ).json()

    file = id + ".json"
    user = {}
    list = []

    for task in todo_url:
        if task.get('userId') == int(id):
            Dict = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user_url.json().get("username")}
            list.append(Dict)
    user[id] = list

    with open(file, "w") as f:
        json.dump(user, f)
