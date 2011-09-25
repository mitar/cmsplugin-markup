from django import template
from django.conf import settings

register = template.Library()

@register.tag
def rendermarkup(parser, token):
    return RenderMarkupNode()

class RenderMarkupNode(template.Node):
    def render(self, context):
        try:
            return context['object'].render(context)
        except:
            if settings.TEMPLATE_DEBUG:
                raise
            else:
                return u''
