# encoding=utf8
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name="django-cmsplugin-tabs",
    version="0.0.1",
    url='http://github.com/MagicSolutions/django-cmsplugin-tabs',
    description="Plugin for Django-CMS that create list of tabs (using jquery ui)",
    long_description=README,

    author='Venelin Stoykov',
    author_email='venelin@magicbg.com',
    packages=[
        'cmsplugin_tabs',
    ],
    package_data={
        'cmsplugin_tabs': [
            'static/cmsplugin_tabs/*.gif',
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
    ],
)
