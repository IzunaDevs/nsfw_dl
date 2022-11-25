"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import random

from nsfw_dl.bases import BaseSearchHTML, BaseSearchXML
from nsfw_dl.errors import NoResultsFound


class GelbooruRandom(BaseSearchHTML):
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


class GelbooruSearch(BaseSearchXML):
    """ Gets a random image with a specific tag from gelbooru. """
    data_format = "xml"

    @staticmethod
    def prepare_url(args):
        """ .... """
        return ("https://www.gelbooru.com/index.php"
                f"?page=dapi&s=post&q=index&tags={args}", {}, {})

    @staticmethod
    def get_image(data):
        """ ... """
        if data:
            if int(data.get('count')) > 0:
                imagelist = [tag.find('file_url').text for tag in data.findall(
                    'post')]
                return random.choice(imagelist)
        raise NoResultsFound
