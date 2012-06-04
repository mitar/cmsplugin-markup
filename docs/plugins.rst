.. _markup plugin API:

Markup Plugin API
=================

At its core, cmsplugin-markup is built around the idea of markup plugins which
can implement different markup implementation for parsing user input. By
default it comes with Markdown_, reST_ and Textile_ plugins available in the
``cmsplugin_markup/plugins/`` directory.

.. _Markdown: http://daringfireball.net/projects/markdown/
.. _reST: http://docutils.sourceforge.net/rst.html
.. _Textile: http://textile.sitemonks.com/

Specifiying Available Plugins
-----------------------------

To determine which markup plugins are available to the user, cmsplugin-markup
looks for a setting ``CMS_MARKUP_OPTIONS``. It expects this to be a tuple in
this format::

    CMS_MARKUP_OPTIONS = (
        'cmsplugin_markup.plugins.markdown',
        'cmsplugin_markup.plugins.textile',
        'cmsplugin_markup.plugins.restructuredtext',
    )

Each entry should be a string and should be a complete path to a Python module
that contains the plugin.

You can also configure what is a default value for markups which support
dynamically rendered output, using ``CMS_MARKUP_RENDER_ALWAYS`` setting (by
default ``True``).

API
---

To be used as a markup plugin, a Python module must contain a class that
defines required methods and attributes. This class must be named ``Markup``.
For example::

    from cmsplugin_markup.plugins import MarkupBase

    class Markup(MarkupBase):
        name = 'Human Readable Name for Plugin'
        identifier = 'internal-plugin-identifier'

        def parse(self, value, context=None, placeholder=None):
            return value

This barebones class contains all the required pieces to work. 

The ``name`` variable is a human readable name and may be of any length. This
is the name that will be presented to the user as the option to choose the
markup language from.

The ``identifier`` variable is stored as a CharField and anything that is
allowed in a CharField is allowed in this. It must be unique across all the
installed markup plugins and may be at most 20 characters long.

The ``parse`` function must accept self, and a value argument. It must accept
also possible Django template rendering context and current placeholder. Those
are given when rendering markup every time the page is displayed is enabled; to
give more information about the context and location in which they are
rendered. This function is where you will implement the actual rendering of
user's input.

There are some additional methods and an attribute if markup supports adding
text plugins. In this case ``text_enabled_plugins`` class attribute should be
set to ``True`` and the following methods should be defined.

``plugin_id_list(self, text)`` should return the list of plugins inserted and
currently used in the markup text.

``replace_plugins(self, text, id_dict)`` should replace references to plugins
in the markup text with new ids.

``plugin_markup(self)`` should return JavaScript code for anonymous function
which construct plugin markup given ``plugin_id``, ``icon_src`` and
``icon_alt`` arguments. It should be marked as safe to prevent escaping.

``plugin_regexp(self)`` should return JavaScript code for anonymous function
which construct plugin regexp given plugin_id. It should be marked as safe to
prevent escaping.

Some markups support dynamically rendered output (like macros) which could be
rendered every time differently. If your markup supports this you can set
``is_dynamic`` to ``True`` and this will then give users an option to enable
rendering of the content every time the page (markup plugin) is displayed
(default value is configured by ``CMS_MARKUP_RENDER_ALWAYS`` setting).
Otherwise the content is rendered only once, when saved.
