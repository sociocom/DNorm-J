# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

import os

from setuptools import find_packages, setup


def read_requirements():
    """parse requirements from requirements.txt."""
    reqs_path = os.path.join("", "requirements.txt")
    with open(reqs_path, "r") as f:
        requirements = [line.rstrip() for line in f]
    return requirements


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="dnorm_j",
    version="0.1.1",
    description="Japanese disease normalizer",
    long_description=readme,
    author="Shogo Ujiie",
    author_email="ujiie@is.naist.jp",
    url="https://github.com/sociocom/DNorm-J",
    license=license,
    install_requires=read_requirements(),
    packages=find_packages(exclude=("tests", "docs")),
)
