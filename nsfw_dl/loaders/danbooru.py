"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class DanbooruRandom(GenericRandom):
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
        return "http://danbooru.donmai.us/posts/random", {}, {}


class DanbooruSearch(GenericSearch):
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
        return f"http://danbooru.donmai.us/posts.json?tags={args}", {}, {}
