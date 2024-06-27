from setuptools import setup, find_packages

setup(
    name='bdl',
    version='0.1',
    description='Bloomberg Data License REST API wrapper',
    author='José Governo',
    author_email='zegoverno@hotmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'requests_oauthlib',
        'pandas'
    ],
)