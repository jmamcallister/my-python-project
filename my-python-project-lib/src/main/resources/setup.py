#from setuptools import setup
from distutils.core import setup
from codecs import open

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

# Get the license from the relevant file
with open(path.join(here, 'LICENSE.txt'), encoding='utf-8') as f:
    license = f.read()

setup(
    name='${project.parent.artifactId}',

    version='${project.parent.version}',

    description='${project-short-description}',

    long_description=long_description,

    author='LM Ericsson Ltd.',

    author_email='info@ericsson.com',

    url='http://www.ericsson.com',

    license=license
)
