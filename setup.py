import os, sys
from setuptools import setup, find_packages

def read_requirements():
        """Parse requirements from requirements.txt."""
        reqs_path = os.path.join('.', 'requirements.txt')
        with open(reqs_path, 'r') as f:
            requirements = [line.rstrip() for line in f]
        return requirements

setup(
    name='dnorm',
    version='0.0.1',
    description='Japanese version of DNorm',
    long_description=readme,
    author='Shogo Ujiie',
    author_email='ujiie@is.naist.jp',
    install_requires=read_requirements(),
    url='https://github.com/sociocom/DNorm-J',
    license=license,
    packages=['dnorm']
)
