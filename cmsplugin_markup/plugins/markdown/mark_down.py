

import logging

from cmsplugin_markup.plugins import MarkupBase
from django.conf import settings
from django.utils.encoding import force_text

log = logging.getLogger(__name__)


class Markup(MarkupBase):

    name = "Markdown"
    identifier = "markdown"

    def parse(self, value, context=None, placeholder=None):
        try:
            import markdown
        except ImportError as err:
            log.error("Can't import markdown: %s", err)
            return force_text(value)
        else:
            # https://python-markdown.github.io/reference/
            return markdown.markdown(force_text(value), extensions=settings.CMS_MARKDOWN_EXTENSIONS)
