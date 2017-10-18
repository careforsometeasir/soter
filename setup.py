from setuptools import setup, find_packages
from codecs import open
from os import path



here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

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
        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='security hash safe storage admin accounts',
    packages=[],
    py_modules=["soteruser"],
    install_requires=['os','binascii','hashlib','json','ast'],

    python_requires='>=3,<4',
)
