"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
__all__ = ['CleanTag']


class CleanTag:
    def __init__(self, tag):
        self.tag = tag
        self.clean()

    def clean(self):
        return (self.tag.format(
                ' ', '_').format('(', '%28').format(')', '%29'))
