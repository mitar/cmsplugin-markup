from django.conf import settings

from django import http
from django import shortcuts
from django.contrib import admin

from cms.models import pluginmodel

from cmsplugin_markup.utils import markup

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
    change_form_template = 'cmsplugin_markup/markup_plugin_change_form.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
            })
        return context

    def get_plugin_urls(self):
        from django.conf.urls.defaults import patterns, url

        # If django-cms has get_plugin_urls feature or not
        urls = getattr(super(MarkupPlugin, self), 'get_plugin_urls', lambda: [])()
        preview_urls = patterns('',
            url(r'^preview/$', admin.site.admin_view(self.preview), name='cmsplugin_markup_preview'),
        )

        return preview_urls + urls

    def preview(self, request):
        if request.method != 'POST':
            return http.HttpResponseNotAllowed(['POST'])
        
        if not shortcuts.get_object_or_404(pluginmodel.CMSPlugin, pk=request.POST.get('plugin_id')).placeholder.has_change_permission(request):
            raise http.Http404
        
        return http.HttpResponse(markup.markup_parser(request.POST.get('text'), request.POST.get('markup')))

plugin_pool.register_plugin(MarkupPlugin)
