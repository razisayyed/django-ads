# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from ads import __version__


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


REQUIREMENTS = [
    'Django>=1.8',
    'django-appconf>=1.0.2',
    'django-sekizai>=0.9.0',
    'django-braces>=1.10.0',
    'django-js-reverse>=0.8.2',
    'Pillow',
]


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='django-ads',
    version=__version__,
    description='Ads Management System for Django Framework',
    long_description=long_description,
    author='Razi Alsayyed',
    author_email='razi.sayed@gmail.com',
    url='https://github.com/razisayyed/django-ads',
    packages=find_packages(),
    license='LICENSE',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
