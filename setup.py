#!/usr/bin/env python

from setuptools import setup

setup(
    name='adminapi',
    url='https://github.com/innogames/serveradmin',
    author='InnoGames System Administration',
    author_email='it@innogames.com',
    packages=['adminapi'],
    version='1.1',
    long_description='Serveradmin client library',
    entry_points={'console_scripts': ['adminapi=adminapi.cli:main']},
)
