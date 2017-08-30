"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom, GenericSearch


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


# WHERE IS THE FUCKIN API DOCS TO DRUNKENPUMKEN TO SEARCH TAGS???
class DrunkenpumkenSearch(GenericSearch):
    """
    Gets a random image with a specific tag from danbooru.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"http://drunkenpumken.booru.org/index.php?page=dapi&s=post&q=index&tags={args}", {}, {}
