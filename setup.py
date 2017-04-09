#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "dnspython",
    "PyYAML"
]

test_requirements = [
    "pip==8.1.2",
    "bumpversion==0.5.3",
    "wheel==0.29.0",
    "watchdog==0.8.3",
    "flake8==2.6.0",
    "tox==2.3.1",
    "coverage==4.1",
    "Sphinx==1.4.8",
    "cryptography==1.7",
    "PyYAML==3.11",
    "pytest==2.9.2"
]

setup(
    name='onionrouter',
    version='0.4.0',
    description="Python Onion Routed Mail Deliveries",
    long_description=readme + '\n\n' + history,
    author="Ehlo Onion",
    author_email='onionmx@lists.immerda.ch',
    url='https://github.com/ehloonion/onionrouter',
    packages=[
        'onionrouter',
    ],
    entry_points={
        "console_scripts": ['onionrouter = onionrouter.onionrouter:main']
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='onionrouter',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
