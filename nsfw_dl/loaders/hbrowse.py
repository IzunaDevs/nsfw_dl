"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""


class HbrowseRandom:
    """ Gets a random image from hbrowse. """
    data_format = "url"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return "http://www.hbrowse.com/random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="highres").get("href")
