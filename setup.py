#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "dnspython>=2.0.0,<3.0.0",
    "PyYAML>=4.2b1",
]

test_requirements = [
    "pip>=19.2",
    "bumpversion==0.5.3",
    "wheel==0.29.0",
    "watchdog==0.8.3",
    "flake8==2.6.0",
    "tox==2.3.1",
    "coverage==4.1",
    "Sphinx==1.4.8",
    "cryptography==3.3.2",
    "PyYAML==6.0",
    "pytest==2.9.2"
]

setup(
    name='onionrouter',
    version='0.6.2',
    description="Python Onion Routed Mail Deliveries",
    long_description=readme,
    author="Ehlo Onion",
    author_email='onionmx@lists.immerda.ch',
    url='https://github.com/ehloonion/onionrouter',
    packages=[
        'onionrouter',
    ],
    entry_points={
        "console_scripts": ['onionrouter = onionrouter.rerouter:main']
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='onionrouter',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
