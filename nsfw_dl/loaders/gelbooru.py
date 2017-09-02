"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.errors import NoResultsFound


class GelbooruRandom:
    """
    Gets a random image from gelbooru.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "https://www.gelbooru.com/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        try:
            return f'https:{data.find(id="image").get("src")}'
        except AttributeError:
            raise AttributeError(str(data))


class GelbooruSearch:
    """
    Gets a random image with a specific tag from gelbooru.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return ("http://furry.booru.org/index.php"
                f"?page=post&s=list&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            images = data.find_all(attrs="thumb")
            if images:
                return random.choice(images).find("img").get("src")
        raise NoResultsFound
