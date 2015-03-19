from django.conf import settings
from django.utils.encoding import smart_bytes, force_text

from cmsplugin_markup.plugins import MarkupBase

class Markup(MarkupBase):

    name = 'Textile'
    identifier = 'textile'

    def parse(self, value, context=None, placeholder=None):
        try:
            import textile
        except ImportError:
            return force_text(value)
        else:
            return textile.textile(value)
