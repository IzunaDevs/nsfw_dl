@echo off
"%SystemDrive%\Python360\python.exe" -m pip install --upgrade codecov
"%SystemDrive%\Python360\python.exe" setup.py test
