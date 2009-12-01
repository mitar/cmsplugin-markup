from django.db import models
from django.utils.translation import ugettext as _
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.conf import settings
from cms.models import CMSPlugin

from cmsplugin_markup import utils

MARKUP_CHOICES = utils.compile_markup_choices(settings.CMS_MARKUP_OPTIONS)

class MarkupField(CMSPlugin):
    body = models.TextField(_('Body'))
    body_html = models.TextField(blank=True)
    markup = models.CharField(
            _('Markup'),
            max_length=20,
            choices=MARKUP_CHOICES
            )

    def __unicode__(self):
        return u'%s' %(truncate_words(strip_tags(self.body_html), 3)[:30]+'...')

    def save(self, *args, **kwargs):
        self.body_html = utils.markup_parser(self.body, self.markup)
        return super(MarkupField, self).save(*args, **kwargs)
