
from cmsplugin_markup.plugins import MarkupBase

class Markup(MarkupBase):

    name = 'Raw HTML'
    identifier = 'html'

    def parse(self, value, context=None, placeholder=None):
        return value
