#!/usr/bin/env python
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.dirname(__file__)

exec(open(os.path.join(here, 'coinmarketcal', 'version.py')).read())
setup(name = "coinmarketcal",
    version = version_strin