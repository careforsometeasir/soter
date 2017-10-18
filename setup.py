from setuptools import setup, find_packages

setup(
    name='soter',
    version='0.1',

    description='A module to store usernames, hashed passwords and salts',

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
    py_modules=["soter"],
    install_requires=['os','binascii','hashlib','json','ast'],

    python_requires='>=3,<4',
)
