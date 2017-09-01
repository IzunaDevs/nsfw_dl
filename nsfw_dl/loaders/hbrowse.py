"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""


class HbrowseRandom:
    """
    Gets a random image from hbrowse.
    """
    reqtype = "get"
    data_format = "url"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://www.hbrowse.com/random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        return data.find(id="highres").get("href")
