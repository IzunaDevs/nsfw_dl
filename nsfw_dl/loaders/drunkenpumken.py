"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom


class DrunkenpumkenRandom(GenericRandom):
    """
    Gets a random image from drunkenpumken.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://drunkenpumken.booru.org/index.php?page=post&s=random", {}, {}
