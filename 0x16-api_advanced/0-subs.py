#!/usr/bin/python3
"""request numbers of subscribers on reddit"""
import requests


def number_of_subscribers(subreddit):
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit),
                           headers={"User-Agent": "holberton"},
                           allow_redirects=False)

    if request.status_code == 200:
        return request.json()["data"]["subscribers"]

    return 0
