# setup.py
from setuptools import setup, find_packages

setup(
    name='df_scrubber',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Martin Hyca',
    author_email='hyca.martin@gmail.com',
    description='A simple package with some(?) utilities for cleaning of Pandas dataframes created for learning purposes.',
    keywords='pandas dataframe cleaning',
)
