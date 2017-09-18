import os
import subprocess

import requests

import nsfw_dl


un = os.environ["PYPI_USERNAME"]
pw = os.environ["PYPI_PASSWORD"]

try:
    remote_ver = requests.get(
        "https://pypi.python.org/pypi/nsfw_dl/json").json()["info"]["version"]

except:  # noqa pylint: disable=bare-except
    remote_ver = "0.0.0"

ver = nsfw_dl.__version__

if ver != remote_ver:
    print("UPLOADING TO PYPI")

    p1 = subprocess.Popen(
        "python3.6 setup.py sdist bdist_egg bdist_wheel".split())
    p1.wait()
    p2 = subprocess.Popen(
        f"twine upload dist/*{ver}* -u {un} -p {pw}".split())
    p2.wait()
