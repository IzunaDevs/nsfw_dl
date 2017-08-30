"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class YandereRandom(GenericRandom):
    """
    Gets a random image from yandere.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "https://yande.re/post/random", {}, {}


class YandereSearch(GenericSearch):
    """
    Gets a random image with a specific tag from yandere.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://yande.re/post.json?tags={args}", {}, {}
