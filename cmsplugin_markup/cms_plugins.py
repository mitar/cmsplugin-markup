from django import http
from django import shortcuts
from django import template
from django.contrib import admin

from cms.models import pluginmodel

from cmsplugin_markup.utils import markup

from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_markup import utils
from cmsplugin_markup.forms import MarkupForm
from cmsplugin_markup.models import MarkupField
from cmsplugin_markup.templatetags import markuptags

class MarkupPlugin(CMSPluginBase):
    model = MarkupField
    name = _('Markup')
    form = MarkupForm
    render_template = 'cmsplugin_markup/markup.html'
    # change_form_template = 'cmsplugin_markup/markup_plugin_change_form.html'

    fieldsets = (
        (None, {
            'fields': ('body', 'markup')
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('dynamic', 'css_class')
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        obj.clean_plugins()
        super(MarkupPlugin, self).save_model(request, obj, form, change)

    def change_view(self, request, object_id, extra_context=None):
        if extra_context is None:
            extra_context = {}

        extra_context.update({
            'text_plugins': [p() for p in plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)],
            'name': 'markupeditor',
            'used_plugins': pluginmodel.CMSPlugin.objects.filter(parent=object_id),
            'markup_plugins': [c() for c in utils.get_list_of_markup_classes().values()],
        })
        return super(MarkupPlugin, self).change_view(request, object_id, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        if extra_context is None:
            extra_context = {}

        extra_context.update({
            'text_plugins': [p() for p in plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)],
            'name': 'markupeditor',
            'markup_plugins': [c() for c in utils.get_list_of_markup_classes().values()],
        })
        return super(MarkupPlugin, self).add_view(request, form_url, extra_context=extra_context);

    def get_plugin_urls(self):
        from django.conf.urls import url

        # If django-cms has get_plugin_urls feature or not
        urls = getattr(super(MarkupPlugin, self), 'get_plugin_urls', lambda: [])()
        preview_urls = [
            url(r'^preview/$', admin.site.admin_view(self.preview), name='cmsplugin_markup_preview'),
        ]

        plugin_urls = []
        for c in utils.get_list_of_markup_classes().values():
            plugin_urls.extend(c().get_plugin_urls())

        return preview_urls + plugin_urls + urls

    def preview(self, request):
        if request.method != 'POST':
            return http.HttpResponseNotAllowed(['POST'])

        try:
            plugin = MarkupField.objects.get(pk=request.POST.get('plugin_id'))
        except MarkupField.DoesNotExist:
            plugin = shortcuts.get_object_or_404(pluginmodel.CMSPlugin, pk=request.POST.get('plugin_id'))

        placeholder = plugin.placeholder

        if not placeholder.has_change_permission(request):
            raise http.Http404
        
        if not request.POST.get('markup'):
            return http.HttpResponse('')

        (content, parser) = markup.markup_parser(request.POST.get('text'), request.POST.get('markup'), template.RequestContext(request, {
                'object': plugin,
                'placeholder': placeholder,
            }), placeholder)

        content += markuptags.content_scripts(parser.get_scripts()) + markuptags.content_stylesheets(parser.get_stylesheets())

        return http.HttpResponse(content)

plugin_pool.register_plugin(MarkupPlugin)
