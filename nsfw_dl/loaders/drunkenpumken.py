"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""


class DrunkenpumkenRandom:
    """ Gets a random image from drunkenpumken. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ ... """
        type(args)
        return ("http://drunkenpumken.booru.org/"
                "index.php?page=post&s=random", {}, {})

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="image").get("src")
