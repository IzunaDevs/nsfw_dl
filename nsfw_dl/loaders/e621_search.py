"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class E621Search(GenericSearch):
    """
    Gets a random image with a specific tag from gelbooru.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://e621.net/post/index.json?page=dapi&s=post&q=index&tags={args}", {}, {}
