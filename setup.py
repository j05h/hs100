# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='hs100',
    version='0.0.1',
    description='Tool for manipulating the TP-Link HS100',
    long_description=readme,
    author='Josh Kleinpeter',
    author_email='josh@kleinpeter.org',
    url='https://github.com/j05h/hs100',
    license=license,
    scripts=['bin/hs100.py'],
    packages=['hs100']
)
