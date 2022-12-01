from setuptools import setup, find_packages


install_requires = [
    'aiohttp>=2.2.0', 'beautifulsoup4>=4.6.0']


try:
    with open('README.rst') as f:
        readme = f.read()
except FileNotFoundError:
    readme = ""


setup(
    name='nsfw_dl',
    author='IzunaDevs',
    author_email='izunadevs@martmists.com',
    url='https://github.com/IzunaDevs/nsfw_dl',
    version='0.4.2',
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
    entry_points={
        'console_scripts': ['nsfw_dl=nsfw_dl.__main__:main',
                            'nsfw-dl=nsfw_dl.__main__:main'],
    },
    platforms='Any',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
