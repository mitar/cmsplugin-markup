cmsplugin-markup's documentation
================================

An extendable markup content plugin for `Django CMS`_. It allows you to use
various markup languages for content. It is extendable through its own markup
plugin system so additional markup languages can be supported. By default it
supports Markdown_, reST_, Textile_ and Creole_ markup languages.

.. _Django CMS: https://www.django-cms.org/
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _reST: http://docutils.sourceforge.net/rst.html
.. _Textile: http://textile.sitemonks.com/
.. _Creole: https://code.google.com/p/python-creole/

There is also a `html` dummy plugin, to add html code directly into a cms page.

Installation
------------

You should install it somewhere Django can find it and add ``cmsplugin_markup``
to ``INSTALLED_APPS``. You can also configure ``CMS_MARKUP_OPTIONS`` setting to
configure which markup plugins you want available in Django CMS.

To install it from PyPi_ run::

    pip install cmsplugin-markup

To install it from source code run::

    python setup.py install

If you want preview functionality in admin to work you have to add something
like the following to your ``urls.py`` file::

    (r'^admin/cms/plugin/markup/', include('cmsplugin_markup.urls')),

This will also allow markup plugins to handle their own additional URLs under
above base URL.

.. _PyPi: http://pypi.python.org/pypi
Add this to your settings::

    MIGRATION_MODULES = {
        'cmsplugin_markup': 'cmsplugin_markup.migrations_django',
    }
    CMS_MARKUP_OPTIONS = (
        'cmsplugin_markup.plugins.markdown',
        'cmsplugin_markup.plugins.textile',
        'cmsplugin_markup.plugins.restructuredtext',
        'cmsplugin_markup.plugins.creole',
    )
    CMS_MARKUP_RENDER_ALWAYS = True

    # see: https://python-markdown.github.io/reference/#extensions
    CMS_MARKDOWN_EXTENSIONS = ()

html plugin
-----------

You can insert html source code with the `html` plugin.

Big warning: If you also activate the `html` plugin, every user with page permissions
can inject javascript code!

To activate, just add it in your settings::

    CMS_MARKUP_OPTIONS = (
        'cmsplugin_markup.plugins.html', # WARNING: javascript code injection will be possible!
        ...
    )

Markup Plugins
--------------

If you need support for some other markup language, you can extend this plugin
through its own :ref:`markup plugin API <markup plugin API>`.

For example, there exists a plugin_ for Trac_ wiki engine with powerful markup
language (with its own macros and plugins).

.. _plugin: https://github.com/mitar/cmsplugin-markup
.. _Trac: http://trac.edgewall.org/

Source Code and Issue Tracker
-----------------------------

For development GitHub_ is used, so source code and issue tracker is found
there_.

.. _GitHub: https://github.com
.. _there: https://github.com/mitar/cmsplugin-markup

Indices and tables
==================
* :ref:`genindex`
* :ref:`search`
