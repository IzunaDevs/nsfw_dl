import os
import subprocess
import nsfw_dl


un = os.environ["PYPI_USERNAME"]
pw = os.environ["PYPI_PASSWORD"]
ver = nsfw_dl.__version__

try:
    subprocess.Popen("python3.6 setup.py build buld_ext build_whl".split())
    subprocess.Popen(f"twine upload build/*{ver}* -u {un} -p {pw}".split())

except:
    pass
