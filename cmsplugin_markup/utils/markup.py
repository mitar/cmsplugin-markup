from django.conf import settings

from cmsplugin_markup.plugins import MarkupBase, MarkupPluginException

def get_list_of_markup_classes(markup_options=settings.CMS_MARKUP_OPTIONS):
    """
    Takes a tuple of python packages that impliment the cmsplugin_markup
    api and return a dict of the objects with identifier as key.
    """
    import sys

    objects = {}

    for markup in markup_options:
        __import__(markup)
        module = sys.modules[markup]

        try:
            # Check for required attributes
            for attribute in ['name', 'identifier']:
                if not hasattr(module.Markup, attribute):
                    raise MarkupPluginException("Markup plugin '%s' is missing '%s' attribute" % (markup, attribute))
            if not issubclass(module.Markup, MarkupBase):
                raise MarkupPluginException("Markup plugin '%s' is not a subclass of MarkupBase")

            objects[module.Markup.identifier] = module.Markup
        except AttributeError:
            raise MarkupPluginException("Markup plugin module '%s' is missing Markup class", (markup,))

    return objects

def compile_markup_choices(markup_options):
    """
    Takes a tuple of python packages that impliment the cmsplugin_markup
    api and makes a tuple of options for the forms.
    """

    choices = []
    objects = get_list_of_markup_classes(markup_options)

    for identifier, markup_object in objects.iteritems():
        choices.append((identifier, markup_object.name))

    return tuple(choices)

def get_markup_object(markup_id):
    """
    Returns an markup object based on its id.
    """

    markup_classes = get_list_of_markup_classes(settings.CMS_MARKUP_OPTIONS)
    return markup_classes[markup_id]()

def markup_parser(value, parser_identifier, context=None, placeholder=None):
    """
    Takes a string and a parser identifier and returns a tuple with string parsed
    by that parser and parser object itself.
    """

    parser = get_markup_object(parser_identifier)
    return (parser.parse(value, context, placeholder), parser)
