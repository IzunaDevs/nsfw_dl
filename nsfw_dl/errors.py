"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
__all__ = ['NoLoader', 'NoResultsFound', 'NoXMLParser',
           'UnsupportedDataFormat']


class NoLoader(Exception):
    """
    Thrown when there is no such loader in the NSFWDL instance
    """
    pass


class NoResultsFound(Exception):
    """
    Thrown when the search found no results for the search.
    """
    pass


class NoXMLParser(Exception):
    """
    Thrown when there is no xml parser.
    """
    pass


class UnsupportedDataFormat(Exception):
    """
    Thrown when there is an unsupported format.
    """
    pass
