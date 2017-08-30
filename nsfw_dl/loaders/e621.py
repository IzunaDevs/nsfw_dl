"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class E621Random(GenericRandom):
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
        return "https://e621.net/post/random", {}, {}


class E621Search(GenericSearch):
    """
    Gets a random image with a specific tag from gelbooru.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://e621.net/post/index.json?page=dapi&s=post&q=index&tags={args}", {}, {}
