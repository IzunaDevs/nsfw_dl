"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""


class TsuminoRandom:
    """ Gets a random image from tsumino. """
    data_format = "url"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "http://www.tsumino.com/Browse/Random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="highres").get("href")
