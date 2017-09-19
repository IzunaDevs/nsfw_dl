"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""


class NhentaiRandom:
    """ Gets a random image from nhentai. """
    data_format = "url"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "http://nhentai.net/random/", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="highres").get("href")
