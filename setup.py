from setuptools import setup, find_packages
from os.path import join, dirname
import BeamFemapGraph
setup(
    name='BeamFemapGraph',
    version=BeamFemapGraph.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
	install_requires=[
    'matplotlib', 'numpy']
)