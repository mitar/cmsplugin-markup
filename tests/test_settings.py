
import os
import tempfile

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
)
MIDDLEWARE_CLASSES = ()

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en","en"),
)
SECRET_KEY = 'fake-key'

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',

    'mptt',
    "cms",

    "cmsplugin_markup",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(tempfile.tempdir or ".", 'cmsplugin_markup_unittest_database'),
    }
}

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'cmsplugin_markup': 'cmsplugin_markup.migrations_django',
}

CMS_MARKUP_OPTIONS = (
    'cmsplugin_markup.plugins.markdown',
    'cmsplugin_markup.plugins.textile',
    'cmsplugin_markup.plugins.restructuredtext',
    'cmsplugin_markup.plugins.creole',
)
CMS_MARKUP_RENDER_ALWAYS = True

CMS_MARKDOWN_EXTENSIONS = ()