"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class KonachanSearch(GenericSearch):
    """
    Gets a random image with a specific tag from konachan.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://konachan.com/post.json?page=dapi&s=post&q=index&tags={args}", {}, {}
