"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchXML


class Rule34Random:
    """ Gets a random image from rule34. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return ("https://rule34.xxx/index.php?page=post&s=random",
                {},
                {"User-Agent": "Mozilla/5.0 Firefox"})

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="image").get("src")


class Rule34Search(BaseSearchXML):
    """ Gets a random image with a specific tag from rule34. """
    data_format = "xml"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return ("https://rule34.xxx/index.php"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})
