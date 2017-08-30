"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class FurrybooruSearch(GenericSearch):
    """
    Gets a random image with a specific tag from furrybooru.
    """
    reqtype = "get"
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"http://furry.booru.org/index.php?page=post&s=list&tags={args}", {}, {}
