
from cmsplugin_markup.plugins import MarkupBase

class Markup(MarkupBase):

    name = 'Pure HTML'
    identifier = 'html'

    def parse(self, value, context=None, placeholder=None):
        return value
