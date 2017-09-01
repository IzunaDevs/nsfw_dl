"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from ..errors import *


class DrunkenpumkenRandom:
    """
    Gets a random image from drunkenpumken.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return ("http://drunkenpumken.booru.org/"
                "index.php?page=post&s=random", {}, {})

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        image = data.find(id="highres").get("href")
        if image is None:
            image = data.find(id="image").get("src")
        return image


# WHERE IS THE FUCKIN API DOCS TO DRUNKENPUMKEN TO SEARCH TAGS???
class DrunkenpumkenSearch:
    """
    Gets a random image with a specific tag from drunkenpumken.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return (f"http://drunkenpumken.booru.org/index.php"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound
