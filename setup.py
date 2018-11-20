from setuptools import setup, find_packages
from time import time


setup(
    name='unixtime',
    version=int(time()),
    author='Andy Palmer',
    author_email='andrew.t.palmer@parker.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['unixtime=unixtime.main:main'],
    },
    install_requires=[
        'argparse'
    ]
)
