"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class XbooruSearch(GenericSearch):
    """
    Gets a random image with a specific tag from yandere.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"http://xbooru.com/index.php?page=dapi&s=post&q=index&tags={args}", {}, {}
