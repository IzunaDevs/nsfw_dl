"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom


class TsuminoRandom(GenericRandom):
    """
    Gets a random image from tsumino.
    """
    reqtype = "get"
    data_format = "url"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://www.tsumino.com/Browse/Random", {}, {}
