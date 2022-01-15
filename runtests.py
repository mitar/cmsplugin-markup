#!/usr/bin/env python3

import os
import shutil
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


def cleanup_temp(temp_dir):
    print("\nCleanup %r: " % temp_dir, end="")
    try:
        shutil.rmtree(temp_dir)
    except (OSError, IOError) as err:
        print("Error: %s" % err)
    else:
        print("OK")


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])

    cleanup_temp(settings.TEMP_DIR)

    sys.exit(bool(failures))


if __name__ == "__main__":
    runtests()
