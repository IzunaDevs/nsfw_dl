"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchHTML


class GelbooruRandom:
    """ Gets a random image from gelbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ .... """
        type(args)
        return "https://www.gelbooru.com/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """ .... """
        try:
            return f'https:{data.find(id="image").get("src")}'
        except AttributeError:
            raise AttributeError(str(data))


class GelbooruSearch(BaseSearchHTML):
    """ Gets a random image with a specific tag from gelbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ .... """
        return ("https://www.gelbooru.com/index.php"
                f"?page=post&s=list&tags={args}", {}, {})
