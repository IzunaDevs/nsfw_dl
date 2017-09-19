"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchXML


class TbibRandom:
    """ Gets a random image from tbib. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "https://www.tbib.org/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return f'https:{data.find(id="image").get("src")}'


class TbibSearch(BaseSearchXML):
    """ Gets a random image with a specific tag from tbib. """
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return ("https://www.tbib.org/index.php?page="
                f"dapi&s=post&q=index&tags={args}", {}, {})
