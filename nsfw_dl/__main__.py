"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import argparse
import nsfw_dl


def download(downloader, args, file):
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download(downloader, args=args)

        if callable(file):
            file = file(img)

        with open(file, "wb") as f:
            f.write(dl.get(img))


# TODO: Add more args.
def main():
    """
    Main entrypoint to nsfw_dl commandline.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--download',
                        help='Download the result to a file.',
                        default=False)
    parser.add_argument('-f', '--file',
                        help="Filename to download to."
                        default=lambda x:x.split("/")[-1])
    ns = parser.parse_args()


if __name__ == '__main__':
    main()
