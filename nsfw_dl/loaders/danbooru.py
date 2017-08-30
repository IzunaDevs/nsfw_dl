"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom


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
