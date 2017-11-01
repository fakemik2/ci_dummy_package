import os
from setuptools import setup, find_packages

def read(*names, **kwargs):
    return open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
).read()

setup(
        name = "ci_dummy",
        version = '0.0.1',
        author = 'fakemik2',
        author_email = 'fakemik2@gmail.com',
        description = 'testing ci services ++',
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires = ['numpy>=1.5.0'],
)
