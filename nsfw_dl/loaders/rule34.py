"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class Rule34Random(GenericRandom):
    """
    Gets a random image from rule34.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://rule34.xxx/index.php?page=post&s=random", {}, {}


class Rule34Search(GenericSearch):
    """
    Gets a random image with a specific tag from rule34.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={args}", {}, {}
