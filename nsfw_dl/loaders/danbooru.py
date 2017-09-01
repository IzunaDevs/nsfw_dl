"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.errors import NoResultsFound


class DanbooruRandom:
    """
    Gets a random image from danbooru.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "https://danbooru.donmai.us/posts/random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        return f'https://danbooru.donmai.us{data.find(id="image").get("src")}'


class DanbooruSearch:
    """
    Gets a random image with a specific tag from danbooru.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://danbooru.donmai.us/posts.json?tags={args}", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound
