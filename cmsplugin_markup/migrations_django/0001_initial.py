# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='MarkupField',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, to='cms.CMSPlugin', parent_link=True, serialize=False, primary_key=True)),
                ('body', models.TextField(verbose_name='Body')),
                ('body_html', models.TextField(blank=True)),
                ('body_scripts', models.TextField(blank=True)),
                ('body_stylesheets', models.TextField(blank=True)),
                ('markup', models.CharField(verbose_name='Markup', max_length=20, default='Creole', choices=[('Creole', 'Creole')])),
                ('dynamic', models.BooleanField(verbose_name='Render every time', default=True, help_text='Should be the content rendered every time the page is displayed or should it be rendered only when saved?')),
                ('css_class', models.CharField(blank=True, verbose_name='CSS class', max_length=255, help_text='Wrap plugin output in a &lt;div&gt; with this CSS class.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
