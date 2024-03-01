#!/usr/bin/env python

from setuptools import setup, find_packages
from goldencage import VERSION

url = "https://github.com/jalu017/perakcage"

long_description = "virtual coin & task management for mobile app (specially for china)"

setup(
    name="perakencage",
    version=VERSION,
    description=long_description,
    maintainer="jalu 017",
    maintainer_email="bebeknganjian@gmail.com",
    url=url,
    long_description=long_description,
    packages=find_packages('.'),
    zip_safe=False,
    install_requires=[
        'requests',
        'youhat',
        'pycrypto',
        'jsonfield',
        'pytz',
        'simplejson',
        'dicttoxml',
        'xmltodict',
        'youchat',
    ]
)
