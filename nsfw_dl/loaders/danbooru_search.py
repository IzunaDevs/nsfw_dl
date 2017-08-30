"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class DanbooruSearch(GenericSearch):
    """
    Gets a random image with a specific tag from danbooru.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"http://danbooru.donmai.us/posts.json?tags={args}", {}, {}
