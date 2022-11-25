"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchHTML


class FurrybooruRandom:
    """ Gets a random image from furrybooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        # https://furry.booru.org/index.php?page=post&s=random
        return ("https://furry.booru.org/index.php?page=post&s=random",
                {},
                {"User-Agent": "Mozilla/5.0 Firefox"})

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="image").get("src")


class FurrybooruSearch(BaseSearchHTML):
    """ Gets a random image with a specific tag from furrybooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return ("https://furry.booru.org/index.php?page=post"
                f"&s=list&tags={args}", {},
                {"User-Agent": "Mozilla/5.0 Firefox"})
