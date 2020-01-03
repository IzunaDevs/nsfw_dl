#!/usr/bin/python3.6

"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import argparse
import sys

import nsfw_dl


def main(argv=sys.argv[1:]):  # pylint: disable=dangerous-default-value
    """
    Main entrypoint to nsfw_dl commandline.
    """
    image = argparse.ArgumentParser()
    image.add_argument('-d', '--download',
                       help='Download the result to a file.',
                       default=False, action="store_true")
    image.add_argument('-f', '--file',
                       help="Filename to download to.",
                       default=lambda x: x.split("/")[-1])
    image.add_argument('-s', '--source',
                       help='Image source to use.',
                       default='Rule34Random')
    image.add_argument('query', help='Tags to use during search.',
                       default='', nargs="*")
    args = image.parse_args(argv[1:])
    download_file = args.download
    file = args.file
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download(args.source, args=args.query)
        if callable(file):
            file = file(img)
        if download_file:
            with open(file, "wb") as f:
                f.write(dl.get(img))
                print(file)
        else:
            print(img)


if __name__ == '__main__':
    main()
