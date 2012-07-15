#!/usr/bin/env python

import os

from setuptools import setup, find_packages

VERSION = '0.2.1'

if __name__ == '__main__':
    setup(
        name = 'cmsplugin-markup',
        version = VERSION,
        description = 'Extendable markup content plugin for Django CMS.',
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
        author = 'Mitar',
        author_email = 'mitar.django@tnode.com',        
        url = 'https://bitbucket.org/mitar/cmsplugin-markup',
        license = 'AGPLv3',
        packages = find_packages(),
        package_data = {},
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
        ],
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            'Django>=1.2',
            'Markdown>=2',
            'Textile>=2.1',
            'docutils>=0.7',
        ],
    )
