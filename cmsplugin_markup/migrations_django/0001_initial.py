# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkupField',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='Body')),
                ('body_html', models.TextField(blank=True)),
                ('body_scripts', models.TextField(blank=True)),
                ('body_stylesheets', models.TextField(blank=True)),
                ('markup', models.CharField(choices=[('Creole', 'Creole')], default='Creole', verbose_name='Markup', max_length=20)),
                ('dynamic', models.BooleanField(default=True, help_text='Should be the content rendered every time the page is displayed or should it be rendered only when saved?', verbose_name='Render every time')),
                ('css_class', models.CharField(verbose_name='CSS class', blank=True, help_text='Wrap plugin output in a &lt;div&gt; with this CSS class.', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
