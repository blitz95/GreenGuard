#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    with open('README.md') as readme_file:
        readme = readme_file.read()
except IOError:
    readme = ''

try:
    with open('HISTORY.md') as history_file:
        history = history_file.read()
except IOError:
    history = ''

install_requires = [
    'baytune>=0.2.3,<0.3',
    'mlblocks>=0.3.0,<0.4',
    'mlprimitives>=0.1.8,<0.2',
    'numpy>=1.15.4,<1.17',
    'pymongo>=3.7.2,<4',
    'scikit-learn>=0.20.1,<0.21',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'coverage>=4.5.1',
    'pytest>=3.4.2',
    'tox>=2.9.1'
]

development_requires = [
    # general
    'bumpversion>=0.5.3',
    'pip>=10.0.0',
    'watchdog>=0.8.3',

    # docs
    'm2r>=0.2.0',
    'Sphinx>=1.7.1',
    'sphinx_rtd_theme>=0.2.4',

    # style check
    'flake8>=3.5.0',
    'isort>=4.3.4',

    # fix style issues
    'autoflake>=1.1',
    'autopep8>=1.3.5',

    # distribute on PyPI
    'twine>=1.10.0',
    'wheel>=0.30.0',

    # Jupyter
    'jupyter>=1.0.0',
]


setup(
    author="MIT Data To AI Lab",
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description=(
        "The GreenGuard project is a collection of end-to-end solutions for machine"
        " learning tasks commonly found in monitoring wind energy production systems."
    ),
    extras_require={
        'test': tests_require,
        'dev': development_requires + tests_require,
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords='wind machine learning green guard',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='greenguard',
    packages=find_packages(include=['greenguard', 'greenguard.*']),
    python_requires='>=3.5',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/D3-AI/GreenGuard',
    version='0.1.1-dev',
    zip_safe=False,
)
