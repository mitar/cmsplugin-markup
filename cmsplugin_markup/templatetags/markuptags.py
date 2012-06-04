from django import template
from django.conf import settings
from django.utils import html, safestring

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

@register.filter
def content_scripts(scripts):
    output = ""
    for script in scripts:
        output += '<script type="%s" src="%s"></script>' % (script.get('type', 'text/javascript'), script['href'])
    return safestring.mark_safe(output)

@register.filter
def content_stylesheets(stylesheets):
    output = ""
    for stylesheet in stylesheets:
        output += 'jQuery.loadStyleSheet("%s", "%s");\n' % (html.escapejs(stylesheet['href']), html.escapejs(stylesheet.get('type', 'text/css')))
    if output:
        output = '<script type="text/javascript">\n' + output + '</script>\n'
    return safestring.mark_safe(output)
