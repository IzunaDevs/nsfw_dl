"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchJSON


class DanbooruRandom:
    """ Gets a random image from danbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "https://danbooru.donmai.us/posts/random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return f'https://danbooru.donmai.us{data.find(id="image").get("src")}'


class DanbooruSearch(BaseSearchJSON):
    """ Gets a random image with a specific tag from danbooru. """
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """ ... """
        return f"https://danbooru.donmai.us/posts.json?tags={args}", {}, {}
