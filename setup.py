#!/usr/bin/env python
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.dirname(__file__)

exec(open(os.path