"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.errors import NoResultsFound


class KonachanRandom:
    """
    Gets a random image from konachan.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "https://konachan.com/post/random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        return f'https:{data.find(id="highres").get("href")}'


class KonachanSearch:
    """
    Gets a random image with a specific tag from konachan.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return ("https://konachan.com/post.json"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound
