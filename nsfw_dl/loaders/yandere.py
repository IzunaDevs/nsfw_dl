"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchJSON


class YandereRandom:
    """ Gets a random image from yandere. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "https://yande.re/post/random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="highres").get("href")


class YandereSearch(BaseSearchJSON):
    """ Gets a random image with a specific tag from yandere. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return f"https://yande.re/post.json?tags={args}", {}, {}
