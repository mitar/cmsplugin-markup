# coding: UTF-8

from __future__ import unicode_literals
from cmsplugin_markup.models import MarkupField
from django.test import TestCase

class BaseTest(TestCase):
    pass

class ModelTest(BaseTest):
    def test_markdown(self):
        instance = MarkupField.objects.create(body="# Markdown Markup!", markup="markdown")
        self.assertEqual(instance.body_html, "<h1>Markdown Markup!</h1>")

    def test_textile(self):
        instance = MarkupField.objects.create(body="h1. Textile Markup!", markup="textile")
        self.assertEqual(instance.body_html, "\t<h1>Textile Markup!</h1>")

    def test_restructuredtext(self):
        instance = MarkupField.objects.create(
            body="The ``ReStructured`` Text...",
            markup="restructuredtext"
        )
        self.assertEqual(
            instance.body_html,
            '<p>The <tt class="docutils literal">ReStructured</tt> Text...</p>\n'
        )

    def test_creole(self):
        instance = MarkupField.objects.create(body="= Creole Markup!", markup="creole")
        self.assertEqual(instance.body_html, "<h1>Creole Markup!</h1>")

    #-----------------------------------------------------------------------------------

    def test_markdown2(self):
        instance = MarkupField.objects.create(body="Markdown: äöüß", markup="markdown")
        self.assertEqual(instance.body_html, "<p>Markdown: äöüß</p>")

    def test_textile2(self):
        instance = MarkupField.objects.create(body="Textile äöüß", markup="textile")
        self.assertEqual(instance.body_html, "\t<p>Textile äöüß</p>")

    def test_restructuredtext2(self):
        instance = MarkupField.objects.create(body="ReSt: äöüß",markup="restructuredtext")
        self.assertEqual(instance.body_html,'<p>ReSt: äöüß</p>\n')

    def test_creole2(self):
        instance = MarkupField.objects.create(body="Creole - äöüß", markup="creole")
        self.assertEqual(instance.body_html, "<p>Creole - äöüß</p>")
