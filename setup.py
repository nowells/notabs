from setuptools import setup, find_packages
from pbs.utils.setuptools import find_package_data

setup(
    name='notabs',
    version='0.1',
    description='',
    author='',
    author_email='',
    packages = find_packages('src'),
    package_dir={'':'src'},
    include_package_data=True,
    package_data = find_package_data('src'),
)
