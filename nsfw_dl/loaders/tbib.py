"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from ..errors import *  # noqa


class TbibRandom:
    """
    Gets a random image from tbib.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "https://www.tbib.org/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        return f'https:{data.find(id="image").get("src")}'


class TbibSearch:
    """
    Gets a random image with a specific tag from tbib.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return (f"https://www.tbib.org/index.php"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound  # noqa
