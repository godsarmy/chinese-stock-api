#!/usr/bin/env python

NAME = 'chinesestockapi_py3'
VERSION = '1.0.0'
DESCRIPTION = 'Python API to get Chinese stock price for Python3.5'
LONG_DESCRIPTION = """\
Library to get Chinese stock price

Supported Engines:
 - Hexun API
 - Sina Finance API
 - Yahoo Finance API

Usage:

 from cstock.request import Requests

 from cstock.hexun_engine import HexunEngine

 engine = HexunEngine()

 requester = Requester(engine)

 stock = requester.request('000626')

 print stock.as_dict()

Github Site: https://github.com/seizetheday/chinese-stock-api.
"""
AUTHOR = 'Roy Liu'
AUTHOR_EMAIL = 'roystd@qq.com'
URL = ''
PLATFORM = 'any'
LICENSE = 'Apache Software License'

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        packages=find_packages(exclude=["test"]),
        platforms=PLATFORM,
        license=LICENSE,
        test_suite='nose.collector'
    )
