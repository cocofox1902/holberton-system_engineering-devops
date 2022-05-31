#!/usr/bin/python3
"""count words"""
import requests


def count_words(subreddit, word_list, nb_word={}, after=None):
    request = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit),
                           headers={"User-Agent": "holberton"},
                           params={"after": after},
                           allow_redirects=False)

    if request.status_code == 404:
        return None

    if request.status_code == 200:
        info = request.json()

        hot_lists = [k.get("data").get("title")
                     for k in info.get("data").get("children")]
        if not hot_lists:
            return None

        word_list = list(dict.fromkeys(word_list))

        if nb_word == {}:
            nb_word = {word: 0 for word in word_list}

        for title in hot_lists:
            split_words = title.split(' ')
            for word in word_list:
                for word_all in split_words:
                    if word_all.lower() == word.lower():
                        nb_word[word] += 1

        if not info.get("data").get("after"):
            sorted_counts = sorted(nb_word.items(),
                                   key=lambda kv: kv[0])
            sorted_counts = sorted(nb_word.items(),
                                   key=lambda kv: kv[1],
                                   reverse=True)
            [print('{}: {}'.format(name, number))
             for name, number in sorted_counts if number != 0]
        else:
            return count_words(subreddit,
                               word_list,
                               nb_word,
                               info.get("data").get("after"))
    else:
        return None
