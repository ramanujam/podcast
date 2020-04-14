# -*- coding: utf-8 -*-

"""Main module."""

import os
import json
import feedparser
from bs4 import BeautifulSoup


def __save_feed(url, path):
    """
    Save the RSS Feed data
    """

    if os.path.isfile(path) and os.access(path, os.R_OK):
        return "Feed already Downloaded"

    print("Either the file is missing or not readable.. loading from source")
    feed = feedparser.parse(url)
    with open(path, "w+") as file_pointer:
        json.dump(feed, file_pointer)

    return "Downloaded"


def get_feed(url, path):
    """
    Get the feed from local store

    """
    saved = __save_feed(url, path)

    if saved:
        with open(path, "r") as file_pointer:
            return json.load(file_pointer)
    else:
        raise ConnectionError("Can't parse and load feed")


def recommendations(url, path="../../data/after_hours.json"):
    """
    Find the recommendations

    """
    feed = get_feed(url, path)

    if 'entries' not in feed:
        print("No entries found, has the structure changed?")
        return {}

    return __get_recommendations(feed)


def __get_recommendations(feed):
    """
    get recommendations from feed
    """

    for entry in feed['entries']:
        for content_type in entry["content"]:
            title, url = __parse_content(content_type)
            res[title] = url

    with open("../../data/recommendations.json", "w+") as file_pointer:
        json.dump(res, file_pointer)

    return res


def __parse_content(content_type):
    """

    """
    title = ""
    url = None

    if "html" in content_type["type"]:
        soup = BeautifulSoup(content_type['value'], 'html.parser')
        if not soup.ul:
            return title, url
        for item in soup.ul.findAll("li"):
            try:
                title = item.a.string
                url = item.a['href']
                print(f'{item.a.string}: {item.a["href"]}')
            except AttributeError:
                title = item.string
                print(f'{item.string}: No URL')

    return title, url


res = recommendations(url="http://feeds.harvardbusiness.org/harvardbusiness/after-hours")
