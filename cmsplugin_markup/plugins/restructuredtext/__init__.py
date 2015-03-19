from django.conf import settings
from django.utils.encoding import smart_bytes, force_text

from cmsplugin_markup.plugins import MarkupBase

class Markup(MarkupBase):

    name = 'ReST (ReStructured Text)'
    identifier = 'restructuredtext'

    def parse(self, value, context=None, placeholder=None):
        try:
            from docutils.core import publish_parts
        except ImportError:
            return force_text(value)
        else:
            docutils_settings = getattr(settings,
                    'RESTRUCTUREDTEXT_FILTER_SETTINGS', {})
            parts = publish_parts(source=smart_bytes(value),
                    writer_name="html4css1",
                    settings_overrides=docutils_settings)
            return force_text(parts["fragment"])
