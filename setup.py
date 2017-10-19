from setuptools import setup, find_packages
from codecs import open
from os import path



here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()

long_description = "=======\nsoteruser\n=======\n---------\nA python module for usernames and passwords.\n---------\n\n**Soter**\n Greek daimon of safety\n\nSoter generates and stores a `hashed <https://en.wikipedia.org/wiki/Cryptographic_hash_function>`_ and `salted <https://en.wikipedia.org/wiki/Salt_(cryptography)>`_ password alongside the associated username.\n\nThe module can then check an entered password against the original.\n\nFor more info and the documentation see `the wiki <https://github.com/careforsometeasir/soteruser/wiki>`_.\n"

setup(
    name='soteruser',
    version=version,

    description='A module to store usernames, hashed passwords and salts',
    long_description=long_description,
    
    url='https://github.com/careforsometeasir/soteruser/',
    
    author='Ryszard Wypijewski',
    author_email='richywypi@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='security hash safe storage admin accounts',
    packages=[],
    py_modules=["soteruser"],
    install_requires=[],

    python_requires='>=2.6,<4',
)
