# encoding=utf8
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name="django-cmsplugin-tabs",
    version="0.0.5",
    url='http://github.com/MagicSolutions/django-cmsplugin-tabs',
    description="Plugin for Django-CMS that create list of tabs (using jquery ui)",
    long_description=README,
    author='Venelin Stoykov',
    author_email='venelin@magicbg.com',
    packages=[
        'cmsplugin_tabs',
        'cmsplugin_tabs.migrations',
    ],
    package_data={
        'cmsplugin_tabs': [
            'templates/cmsplugin_tabs/*.html',
            'static/cmsplugin_tabs/js/*.js',
            'locale/bg/LC_MESSAGES/django.*',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django>=1.3',
        'django-cms',
        'django-tinymce',
    ],
)
