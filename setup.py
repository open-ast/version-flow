import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'Readme.rst')) as f:
    README = f.read()

setup(
    name='version-flow',
    description="",
    long_description=README,
    keywords='A tool to generate version according to PEP-440',
    version='0.1.1',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite='version_flow.tests',
)
