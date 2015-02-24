Developer info
==============

setup test environment
----------------------

    ~$ virtualenv ~/cms_markup_env
    ~$ cd cms_markup_env/
    ~/cms_markup_env$ source bin/activate
    (cms_markup_env)~/cms_markup_env$ pip install -e git+git@github.com:jedie/cmsplugin-markup.git#egg=cmsplugin-markup

To run unittests:

    ~$ cd cms_markup_env/
    ~/cms_markup_env$ source bin/activate
    (cms_markup_env)~/cms_markup_env$ cd src/cmsplugin-markup
    (cms_markup_env)~/cms_markup_env$ ./setup.py test

