"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class YandereSearch(GenericSearch):
    """
    Gets a random image with a specific tag from yandere.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://yande.re/post.json?tags={args}", {}, {}
