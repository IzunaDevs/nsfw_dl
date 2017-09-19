"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchJSON


class LolibooruRandom:
    """ Gets a random image from lolibooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "https://lolibooru.moe/post/random/", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="highres").get("href")


class LolibooruSearch(BaseSearchJSON):
    """ Gets a random image with a specific tag from lolibooru. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return f"https://lolibooru.moe/post/index.json?tags={args}", {}, {}
