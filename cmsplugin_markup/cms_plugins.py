from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_markup.models import MarkupField
from cmsplugin_markup.forms import MarkupForm

class MarkupPlugin(CMSPluginBase):
    model = MarkupField
    name = _('Markup')
    form = MarkupForm
    render_template = 'cmsplugin_markup/markup.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
            })
        return context

plugin_pool.register_plugin(MarkupPlugin)
