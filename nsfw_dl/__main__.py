"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import argparse
import sys

import nsfw_dl


def download(downloader, args, file, download):
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download(downloader, args=args)

        if callable(file):
            file = file(img)

        if download:
            with open(file, "wb") as f:
                f.write(dl.get(img))
                print(file)

        else:
            print(img)


# TODO: Add more args.
def main(argv):
    """
    Main entrypoint to nsfw_dl commandline.
    """
    parser = argparse.ArgumentParser()
    image = argparse.ArgumentParser()
    parser.add_argument("action", choices=["image", "sources"])

    image.add_argument('-d', '--download',
                       help='Download the result to a file.',
                       default=False, action="store_true")
    image.add_argument('-f', '--file',
                       help="Filename to download to.",
                       default=lambda x: x.split("/")[-1])
    image.add_argument('source', help="Image source to use.")
    image.add_argument('query', help="Tags to use during search.",
                       default='', nargs="*")

    args = parser.parse_args(argv)

    if args.action == "sources":
        sources = "\n".join("\n".join(v for v in source) for source in
                            nsfw_dl.SOURCES)
        print(sources)

    else:
        args = image.parse_args(argv[1:])
        download(args.source, args.query, args.file, args.download)


if __name__ == '__main__':
    main(sys.argv[1:])
