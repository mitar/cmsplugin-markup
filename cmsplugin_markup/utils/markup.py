
def get_list_of_markup_objects(markup_options):
    """
    Takes a tuple of python packages that impliment the cmsplugin_markup
    api and return a dict of the objects with identifier as key.
    """
    import sys

    objects = {}

    for markup in markup_options:
        try:
            __import__(markup)
            module = sys.modules[markup]
        except ImportError:
            continue

        try:
            # Check for required attributes
            if not hasattr(module.Markup, 'name'):
                continue
            if not hasattr(module.Markup, 'identifier'):
                continue
            if not hasattr(module.Markup, 'parse'):
                continue

            objects[module.Markup.identifier] = module.Markup
        except AttributeError:
            continue
    return objects

def compile_markup_choices(markup_options):
    """
    Takes a tuple of python packages that impliment the cmsplugin_markup
    api and makes a tuple of options for the forms.
    """

    choices = []
    objects = get_list_of_markup_objects(markup_options)

    for identifier, markup_object in objects.iteritems():
        choices.append((identifier, markup_object.name))

    return tuple(choices)

def markup_parser(value, parser_identifier):
    """
    Takes a string and a parser identifier and returns a string parsed
    by that parser. If anything goes wrong it returns the original string
    """
    from django.conf import settings

    markup_objects = get_list_of_markup_objects(settings.CMS_MARKUP_OPTIONS)
    obj = markup_objects[parser_identifier]()

    return markup_objects[parser_identifier]().parse(value)
