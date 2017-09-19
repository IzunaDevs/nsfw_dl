"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchJSON


class KonachanRandom:
    """
    Gets a random image from konachan.
    """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "https://konachan.com/post/random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return f'https:{data.find(id="highres").get("href")}'


class KonachanSearch(BaseSearchJSON):
    """ Gets a random image with a specific tag from konachan. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return ("https://konachan.com/post.json"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})
