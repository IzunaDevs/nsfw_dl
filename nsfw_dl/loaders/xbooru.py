"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.errors import NoResultsFound


class XbooruRandom:
    """
    Gets a random image from xbooru.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://xbooru.com/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        return data.find(id="image").get("src")


class XbooruSearch:
    """
    Gets a random image with a specific tag from xbooru.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return (f"http://xbooru.com/index.php"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            if int(data.find('posts')['count']) > 0:
                imagelist = [tag.get('file_url') for tag in data.find_all(
                    'post')]
                return random.choice(imagelist)
        raise NoResultsFound
