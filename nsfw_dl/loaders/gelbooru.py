"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.bases import BaseSearchHTML
from nsfw_dl.errors import NoResultsFound


class GelbooruRandom:
    """ Gets a random image from gelbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ .... """
        type(args)
        return "https://www.gelbooru.com/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """ .... """
        try:
            return f'https:{data.find(id="image").get("src")}'
        except AttributeError:
            raise AttributeError(str(data))


class GelbooruSearch(BaseSearchHTML):
    """ Gets a random image with a specific tag from gelbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ .... """
        return ("https://www.gelbooru.com/index.php"
                f"?page=post&s=list&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """ ... """
        if data:
            images = data.find_all(attrs="thumbnail-preview")
            if images:
                return random.choice(images).find("img").get("src")
        raise NoResultsFound
