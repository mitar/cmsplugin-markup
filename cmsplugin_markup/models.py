from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.conf import settings
from cms.utils.compat.dj import python_2_unicode_compatible

from cms.models import CMSPlugin

from cmsplugin_markup import utils


MARKUP_CHOICES = utils.compile_markup_choices(settings.CMS_MARKUP_OPTIONS)


@python_2_unicode_compatible
class MarkupField(CMSPlugin):
    body = models.TextField(_('Body'))
    body_html = models.TextField(blank=True)
    body_scripts = models.TextField(blank=True)
    body_stylesheets = models.TextField(blank=True)
    markup = models.CharField(
        _('Markup'),
        max_length=20,
        choices=MARKUP_CHOICES,
        default=MARKUP_CHOICES[0][0] if len(MARKUP_CHOICES) == 1 else models.NOT_PROVIDED,
    )
    dynamic = models.BooleanField(_('Render every time'), default=settings.CMS_MARKUP_RENDER_ALWAYS, help_text=_('Should be the content rendered every time the page is displayed or should it be rendered only when saved?'))
    css_class = models.CharField(_('CSS class'), max_length=255, blank=True, help_text=_('Wrap plugin output in a &lt;div&gt; with this CSS class.'))

    search_fields = ('body_html',)

    def __str__(self):
        content = "<strong>%s</strong>: %s" % (
            self.markup,
            Truncator(strip_tags(self.body_html)).chars(30, html=True)
        )
        return mark_safe(content)

    def save(self, *args, **kwargs):
        # We store it in any case to also check the parser for possible exceptions and to use it for __unicode__
        (content, parser) = utils.markup_parser(self.body, self.markup)
        self.body_html = content
        self.body_scripts = '\n'.join(parser.get_scripts())
        self.body_stylesheets = '\n'.join(parser.get_stylesheets())
        if not utils.get_markup_object(self.markup).is_dynamic:
            self.dynamic = False
        return super(MarkupField, self).save(*args, **kwargs)

    def render(self, context):
        if self.dynamic:
            (content, parser) = utils.markup_parser(self.body, self.markup, context, context.get('placeholder'))
            context['markup_scripts'] = context.get('markup_scripts', []) + parser.get_scripts()
            context['markup_stylesheets'] = context.get('markup_stylesheets', []) + parser.get_stylesheets()
            return mark_safe(content)
        else:
            context['markup_scripts'] = context.get('markup_scripts', []) + self.body_scripts.split('\n')
            context['markup_stylesheets'] = context.get('markup_stylesheets', []) + self.body_stylesheets.split('\n')
            return mark_safe(self.body_html)

    def clean_plugins(self):
        ids = utils.plugin_id_list(self.body, self.markup)
        plugins = CMSPlugin.objects.filter(parent=self)
        for plugin in plugins:
            if not str(plugin.pk) in ids:
                plugin.delete() #delete plugins that are not referenced in the markup anymore

    def post_copy(self, old_instance, ziplist):
        """
        Fix references to plugins
        """

        replace_ids = {}
        for new, old in ziplist:
            replace_ids[old.pk] = new.pk

        try:
            old_body = old_instance.markupfield.body
        except AttributeError:
            # FIXME: AttributeError: 'CMSPlugin' object has no attribute 'markupfield'
            # see: https://github.com/mitar/cmsplugin-markup/issues/10
            return
        else:
            self.body = utils.replace_plugins(old_body, replace_ids, self.markup)
            self.save()
