from django.conf import settings
from django.utils.encoding import smart_str, force_unicode

class Markup(object):

    name = 'Markdown'
    identifier = 'markdown'

    def parse(self, value):
        try:
            import markdown
        except ImportError:
            return force_unicode(value)
        else:
            if hasattr(markdown, 'version'):
                extensions = settings.CMS_MARKDOWN_EXTENSIONS
                if len(extensions) > 0 and extensions[0] == "safe":
                    extensions = extensions[1:]
                    safe_mode = True
                else:
                    safe_mode = False

                if getattr(markdown, 'version_info', None) < (1,7):
                    return force_unicode(markdown.markdown(smart_str(value),
                                extensions, safe_mode=safe_mode))
                else:
                    return markdown.markdown(force_unicode(value), extensions,
                                safe_mode=safe_mode)
            else:
                return force_unicode(markdown.markdown(smart_str(value)))
