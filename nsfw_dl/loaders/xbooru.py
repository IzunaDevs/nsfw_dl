"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchXML


class XbooruRandom:
    """ Gets a random image from xbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "http://xbooru.com/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="image").get("src")


class XbooruSearch(BaseSearchXML):
    """ Gets a random image with a specific tag from xbooru. """
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return ("http://xbooru.com/index.php?page=dapi"
                f"&s=post&q=index&tags={args}", {}, {})
