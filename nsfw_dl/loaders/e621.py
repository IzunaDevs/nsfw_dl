"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchJSON


class E621Random:
    """ Gets a random image from e621. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "https://e621.net/post/random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="highres").get("href")


class E621Search(BaseSearchJSON):
    """ Gets a random image with a specific tag from e621. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return ("https://e621.net/post/index.json?page=dapi&s="
                f"post&q=index&tags={args}", {}, {})
