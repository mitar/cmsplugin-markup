Developer info
==============

setup test environment
----------------------

Create virtual env::

    ~$ virtualenv ~/cms_markup_env
    ~$ cd cms_markup_env/
    ~/cms_markup_env$ source bin/activate

Install as editable from git, read-only::

    (cms_markup_env)~/cms_markup_env$ pip install -e git+https://github.com/mitar/cmsplugin-markup.git#egg=cmsplugin-markup

If you have git write access::

    (cms_markup_env)~/cms_markup_env$ pip install -e git+git@github.com:mitar/cmsplugin-markup.git#egg=cmsplugin-markup

To run unittests::

    ~$ cd cms_markup_env/
    ~/cms_markup_env$ source bin/activate
    (cms_markup_env)~/cms_markup_env$ cd src/cmsplugin-markup
    (cms_markup_env)~/cms_markup_env$ ./setup.py test

