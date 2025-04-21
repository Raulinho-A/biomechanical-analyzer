from setuptools import setup, find_packages

setup(
    name='biomechanical_analyzer',
    version='0.1.0',
    packages=find_packages(include=['analyzer', 'analyzer.*']),
)