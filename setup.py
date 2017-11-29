#!/usr/bin/env python3

""" This is the setup.py script for setting up the package and fulfilling any
necessary requirements.
"""

from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

# Set the home path of the setup script/package
home = path.abspath(path.dirname(__file__))
name = 'HTSeqAnalysis'


def readme():
    """Get the long description from the README file."""
    with open(path.join(home, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name=name,
    author='Shaurita Hutchins & Robert Gilmore',
    description="HTSeq analysis",
    version='0.1',
    long_description=readme(),
    url='https://github.com/datasnakes/impulsivity-htseq-analysis',
    license='',
    keywords='science lab pyschiatry rnaseq',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
    # Packages will be automatically found if not in this list.
    packages=find_packages(),
    package_data={'HTSeqAnalysis': ['pbsjob/temp.pbs']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
                'htseq-count-cluster=HTSeqAnalysis.htseq_count_cluster:main'
                ]
    },
    zip_safe=False
#    test_suite='nose.collector',
#    tests_require=['nose']
)