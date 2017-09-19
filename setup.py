from nsfw_dl import __version__
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


install_requires = [
    'aiohttp>=2.2.0', 'beautifulsoup4>=4.6.0',
    'lxml>=3.8.0']


try:
    with open('README.rst') as f:
        readme = f.read()
except FileNotFoundError:
    readme = ""


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)


# TODO: Change classifiers on this.
setup(name='nsfw_dl',
      author='IzunaDevs',
      author_email='izunadevs@martmists.com',
      url='https://github.com/IzunaDevs/nsfw_dl',
      version=__version__,
      packages=find_packages(),
      license='MIT',
      description='Python 3 package for downloading nsfw images.',
      long_description=readme,
      maintainer_email='izunadevs@martmists.com',
      download_url='https://github.com/IzunaDevs/nsfw_dl',
      include_package_data=True,
      install_requires=install_requires,
      tests_require=['pytest', 'flake8', 'pyflakes', 'coverage',
                     'isort', 'pytest-cov', 'pytest-mock',
                     'pytest-timeout', 'pytest-asyncio',
                     'pylint'],
      platforms='Any',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ],
      cmdclass=dict(test=PyTest))
