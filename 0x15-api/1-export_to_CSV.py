#!/usr/bin/python3
""" 1 - export to CSV """
import requests
import sys
import csv

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(id))
    todo_url = requests.get("https://jsonplaceholder.typicode.com/todos")
    name = user_url.json().get("username")

    file = id + ".csv"

    with open(file, "w") as f:
        writer = csv.writer(f,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for task in todo_url.json():
            if task.get('userId') == int(id):
                writer.writerow([id,
                                 name,
                                 str(task.get("completed")),
                                 task.get("title")])
