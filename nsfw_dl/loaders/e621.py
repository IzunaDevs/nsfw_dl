"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.bases import BaseSearchJSON
from nsfw_dl.errors import NoResultsFound


class E621Random:
    """ Gets a random image from e621. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return ("https://e621.net/posts/random.json?tags=", {},
                {"User-Agent": "Mozilla/5.0 Firefox"})

    @staticmethod
    def get_image(data):
        """ ... """
        return data['post']['file']['url']


class E621Search(BaseSearchJSON):
    """ Gets a random image with a specific tag from e621. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return (f"https://e621.net/posts.json?tags={args}",
                {},
                {"User-Agent": "Mozilla/5.0 Firefox"})

    @staticmethod
    def get_image(data):
        """ ... """
        if data:
            return random.choice(data['posts'])['file']['url']
        raise NoResultsFound
