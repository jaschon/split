#!/usr/bin/env python3

import os
from setuptools import setup
import splity

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "splity",
    version = splity.__version__,
    author = splity.__author__,
    description = (splity.__doc__,),
    keywords = "pdf, split, join",
    url = "https://github.com/jaschon/split",
    packages=['splity', 'bin'],
    long_description=read('README.md'),
    install_requires=read('requirements.txt').splitlines(),
    scripts=['bin/splity',],
)
