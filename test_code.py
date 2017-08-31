import os
import subprocess
import re


def test_flake8():
    proc = subprocess.Popen("flake8", stdout=subprocess.PIPE)

    proc.wait()

    out = proc.stdout.read().decode()

    lines = [l.strip() for l in out.split("\n")if l]

    print(out)

    assert not bool(lines)


def test_pylint():
    proc = subprocess.Popen(("pylint --disable=missing-docstring,"
                             "invalid-name,redefined-builtin,too-many-branches"
                             ",no-name-in-module,protected-access,"
                             "attribute-defined-outside-init,arguments-differ,"
                             "too-many-instance-attributes,import-error"
                             ",parse-error,too-few-public-methods,exec-used,"
                             "fixme,cell-var-from-loop,too-many-locals,"
                             "too-many-arguments,too-many-statements,"
                             "no-member,unused-argument,redefined-outer-name,"
                             "broad-except utils cogs website").split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    proc.wait()

    out = proc.stdout.read().decode()

    print(out)

    last_line = [l for l in out.split("\n")if l][-1]

    m = re.match(r"Your code has been rated at 10\.00\/10", last_line.strip())

    assert m is not None
