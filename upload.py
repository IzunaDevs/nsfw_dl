import os
import subprocess

import requests

import nsfw_dl


un = os.environ["PYPI_USERNAME"]
pw = os.environ["PYPI_PASSWORD"]

remote_ver = requests.get(
    "https://pypi.python.org/pypi/nsfw_dl/json").json()["info"]["version"]
ver = nsfw_dl.__version__

if ver != remote_ver:
    p1 = subprocess.Popen(
            "python3.6 setup.py build buld_ext build_whl".split(),
            stdout=subprocess.PIPE)
    p1.wait()
    print(p1.stdout.read())
    p2 = subprocess.Popen(
            f"twine upload build/*{ver}* -u {un} -p {pw}".split(),
            stdout=subprocess.PIPE)
    p2.wait()
    print(p2.stdout.read())
