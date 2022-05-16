#!/usr/bin/python3
""" 3 - dictionary of list of dictionaries """
import requests
import json

if __name__ == "__main__":
    user_url = (requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )).json()
    todo_url = (requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )).json()

    file = "todo_all_employees" + ".json"
    users = {}

    for user in user_url:
        list = []
        for task in todo_url:
            if task.get('userId') == user.get('id'):
                Dict = {"username": user.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")}
                list.append(Dict)
        users[user.get('id')] = list

    with open(file, "w") as f:
        json.dump(users, f)
