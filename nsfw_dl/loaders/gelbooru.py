"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class GelbooruRandom(GenericRandom):
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
        return "http://www.gelbooru.com/index.php?page=post&s=random", {}, {}


class GelbooruSearch(GenericSearch):
    """
    Gets a random image with a specific tag from gelbooru.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags={args}", {}, {}
