"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import argparse


# TODO: Add more args.
def main(argv):
    """
    Main entrypoint to nsfw_dl commandline.
    """
    type(argv)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--download',
        help='Download the result to a file.',
        default=False)
    ns = parser.parse_args()
    type(ns)


if __name__ == '__main__':
    main()
