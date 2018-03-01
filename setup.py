from setuptools import setup, find_packages

setup(
    name='pycatastro',
    version='0.1.3',
    packages=find_packages(),
    url='https://github.com/gisce/pycatastro',
    license='GPLv3',
    author='GISCE-TI, SL',
    author_email='devel@gisce.net',
    install_requires=[
        'requests',
        'xmltodict',
    ],
    description='Module for Spanish Catastro'
)
