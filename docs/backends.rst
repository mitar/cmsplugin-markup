.. _backend-api:

cmsplugin-markup backends
=========================

At its core, cmsplugin-markup is built around the idea of pluggable backends which can impliment different markup implimentations for parsing user input. By default it comes with Markdown, Textile and ReST Backends available in the cmsplugin_markup/plugins/ directory.

Specifiying available backends
------------------------------
To determine which MarkUp options to give to the user, cmsplugin-markup looks for a setting called CMS_MARKUP_OPTIONS. It expects this to be a tuple in this format::

    CMS_MARKUP_OPTIONS = (
        'cmsplugin_markup.plugins.markdown',
        'cmsplugin_markup.plugins.textile',
        'cmsplugin_markup.plugins.restructuredtext',
        )

Each entry should be a string and should be a complete path to a python package that contains the required attributes.

Backend API
-----------

To be used as a MarkUp backend, a python package must be laid out in a specific fashion and contain a class that must implement the following methods and variables. This class must be named Markup. An example class is below.::

    class Markup(object):
        name = 'Human Readable Name for the Mark Up'
        identifier = 'Internal Identifier for Mark Up'

        def parse(self, value):
            return value

This barebones class contains all the required pieces to work. 

The ``name`` variable is a human readable name and may be any length. This is the name that will be presented to the user as the option. 

The ``identifier`` variable is stored as a CharField and anything that is allowed in a CharField is allowed in this. It must be unique across all the installed MarkUp Parsers and may be at most 20 characters long. 

The ``parse`` function must accept self, and a value argument. This function is where you will impliment the actual parsing of the user's input. At this point in time this function should fail silently and simply return an unchanged string. This might change in the future.

Directory Layout
~~~~~~~~~~~~~~~~

A MarkUp Backend Package should be laid out as follows

backend_name/
- __init__.py
- optional_class.py

The __init__.py file should either contain the Markup class definition, or should import it from an optional python file in the same directory. The optional file may be named anything.
