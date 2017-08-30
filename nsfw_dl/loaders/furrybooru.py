"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class FurrybooruRandom(GenericRandom):
    """
    Gets a random image from furrybooru.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://furry.booru.org/index.php?page=post&s=random", {}, {}


class FurrybooruSearch(GenericSearch):
    """
    Gets a random image with a specific tag from furrybooru.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"http://furry.booru.org/index.php?page=post&s=list&tags={args}", {}, {}
