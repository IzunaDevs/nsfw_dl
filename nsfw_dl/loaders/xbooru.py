"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom


class XbooruRandom(GenericRandom):
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
        return "http://xbooru.com/index.php?page=post&s=random", {}, {}
