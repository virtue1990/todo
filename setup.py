# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = '1.0.0'

'''
To install cryptography, which pyOpenSSL depends on:

>>> sudo apt-get install libssl-dev libffi-dev

'''

setup(
    name="server_todo",
    version=__version__,
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="test for use",
    long_description="flask structure and use ",
    author="virtue",
    author_email="virtue2013@sina.cn",
    include_package_data=True,
    zip_safe=False,
    license="Proprietary",
    keywords=("slack", "egg"),
    platforms="any",
    install_requires=['requests','flask'],
    entry_points={},
)
