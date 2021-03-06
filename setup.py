# -*- coding: utf-8 -*-
"""Setup module for flask taxonomy."""
import os

from setuptools import setup

readme = open('README.md').read()
history = open('CHANGES.md').read()
OAREPO_VERSION = os.environ.get('OAREPO_VERSION', '3.3.0')


install_requires = [
    'deepmerge',
    'redis',
    'pika'
]

tests_require = [
    'deepmerge'
]

extras_require = {
    'tests': [
        *tests_require,
        'oarepo[tests]~={version}'.format(
            version=OAREPO_VERSION)],
    'tests-es7': [
        *tests_require,
        'oarepo[tests-es7]~={version}'.format(
            version=OAREPO_VERSION)],
}

setup_requires = [
    'pytest-runner>=2.7',
]

g = {}
with open(os.path.join('oarepo_health_check', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name="oarepo_health_check",
    version=version,
    url="https://github.com/oarepo/oarepo-dc",
    license="MIT",
    author="Alzbeta Pokorna",
    author_email="alzbeta.pokorna@cesnet.cz",
    description="DCTerms support for OARepo (just selected props)",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=['oarepo_health_check'],
    entry_points={
        'invenio_base.apps': [
            'oarepo_health_check = oarepo_health_check:OARepoHealthCheck'
        ],
        'invenio_base.api_apps': [
            'oarepo_health_check = oarepo_health_check:OARepoHealthCheck'
        ]
    },
    include_package_data=True,
    setup_requires=setup_requires,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
