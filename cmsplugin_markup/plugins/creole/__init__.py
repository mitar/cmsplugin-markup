
from cmsplugin_markup.plugins import MarkupBase

class Markup(MarkupBase):

    name = 'Creole'
    identifier = 'creole'

    def parse(self, value, context=None, placeholder=None):
        try:
            import creole
        except ImportError:
            return value
        else:
            return creole.creole2html(value)
