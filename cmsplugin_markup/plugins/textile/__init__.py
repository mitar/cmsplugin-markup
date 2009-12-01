from django.conf import settings
from django.utils.encoding import smart_str, force_unicode

class Markup(object):

    name = 'Textile'
    identifier = 'textile'

    def parse(self, value):
        try:
            import textile
        except ImportError:
            return force_unicode(value)
        else:
            return force_unicode(textile.textile(smart_str(value),
                encoding='utf-8', output='utf-8'))
