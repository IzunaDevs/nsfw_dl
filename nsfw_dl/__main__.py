#!/usr/bin/python3.8

"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
import argparse
import asyncio
import sys
import os

import nsfw_dl


async def main(argv=None):  # pylint: disable=dangerous-default-value
    """
    Main entrypoint to nsfw_dl commandline.
    """
    image = argparse.ArgumentParser()
    image.add_argument('-d', '--download',
                       help='Download the result to a file.',
                       default=False)
    image.add_argument('-f', '--file',
                       help="Filename to download to.",
                       default=lambda x: x.split("/")[-1])
    image.add_argument('-s', '--source',
                       help='Image source to use.',
                       default='')
    image.add_argument('query', help='Tags to use during search.',
                       default='', nargs="*")
    args = image.parse_args(argv)
    if args.source == '':
        print("Usage: " + os.path.basename(sys.argv[0]) + " [-d/--download]"
              " [-f/--file ...] [-s/--source ...] [query]")
        print("Where first ... is the file name you want, second ... "
              "is the source where source can be:")
        sources = "\n".join("\n".join(v for v in source) for source in
                            nsfw_dl.SOURCES.values())
        print(sources)
        print("And query is what you want to search for.")
    else:
        download_file = args.download
        file = args.file
        async with nsfw_dl.NSFWDL() as dl:
            img = await dl.download(args.source, args=" ".join(args.query))
            if callable(file):
                file = file(img)
            if download_file:
                with open(file, "wb") as f:
                    f.write(dl.get(img))
                    print(file)
            else:
                print(img)


if __name__ == '__main__':
    try:
        asyncio.run(main(argv=sys.argv[1:]))
    except KeyboardInterrupt:
        pass
