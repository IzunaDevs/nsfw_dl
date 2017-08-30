"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


class TbibRandom(GenericRandom):
    """
    Gets a random image from tbib.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://www.tbib.org/index.php?page=post&s=random", {}, {}


class TbibSearch(GenericSearch):
    """
    Gets a random image with a specific tag from tbib.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return (f"http://www.tbib.org/index.php"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})
