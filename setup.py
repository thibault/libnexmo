import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='libnexmo',
    version='1.0.1',
    packages=['libnexmo'],
    include_package_data=True,
    license='MIT',
    description='A simple python wrapper around the Nexmo API',
    long_description=README,
    url='https://github.com/thibault/libnexmo',
    author='Thibault Jouannic',
    author_email='thibault@miximum.fr',
    setup_requires=('setuptools'),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
