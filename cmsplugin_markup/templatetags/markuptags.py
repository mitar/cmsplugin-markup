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

@register.tag
def renderstylesheets(parser, token):
    return RenderMarkupStylesheetsNode()

class RenderMarkupStylesheetsNode(template.Node):
    def render(self, context):
        if 'markup_stylesheets' in context:
            stylesheets = "".join(context['markup_stylesheets'])
            del context['markup_stylesheets']
            return stylesheets
        else:
            return u''

@register.tag
def renderscripts(parser, token):
    return RenderMarkupScriptsNode()

class RenderMarkupScriptsNode(template.Node):
    def render(self, context):
        if 'markup_scripts' in context:
            scripts = "".join(context['markup_scripts'])
            del context['markup_scripts']
            return scripts
        else:
            return u''
