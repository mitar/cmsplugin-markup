from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import smart_bytes, force_text

from cmsplugin_markup.plugins import MarkupBase


class Markup(MarkupBase):

    name = 'Markdown'
    identifier = 'markdown'

    def parse(self, value, context=None, placeholder=None):
        try:
            import markdown
        except ImportError:
            return force_text(value)
        else:
            if hasattr(markdown, 'version'):
                extensions = settings.CMS_MARKDOWN_EXTENSIONS
                if len(extensions) > 0 and extensions[0] == "safe":
                    extensions = extensions[1:]
                    safe_mode = True
                else:
                    safe_mode = False

                if getattr(markdown, 'version_info', None) < (1,7):
                    return force_text(markdown.markdown(smart_bytes(value),
                                extensions, safe_mode=safe_mode))
                else:
                    return markdown.markdown(force_text(value), extensions,
                                safe_mode=safe_mode)
            else:
                return force_text(markdown.markdown(smart_bytes(value)))
