import io
import os

from setuptools import setup


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

setup(
    name='RecMet',
    url='https://github.com/rijulizer/RecMet',
    author='Riju Mukherjee',
    author_email='riju11.mukherjee@gmail.com',
    packages=['RecMet'],
    install_requires=['numpy',
        'pandas']
    ,
    license='Apache',
    version='0.0.1',
    description='Evaluation metrics for recommender systems',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)