django-cmsplugin-tabs
=====================

Plugin for Django-CMS that create list of tabs

INSTALLATION
------------

You can simply install it with pip like this:

    pip install git+https://github.com/MagicSolutions/django-cmsplugin-tabs.git#egg=django-cmsplugin-tabs


After that you must add it to installed apps:

    INSTALLED_APPS = (
        ...
        'cmsplugin_tabs',
        ...
    )

If you are using South you need to put add this in `SOUTH_MIGRATION_MODULES`:

    SOUTH_MIGRATION_MODULES = {
        ...
        'cmsplugin_tabs': 'cmsplugin_tabs.south_migrations',
        ...
    }


CONFIGURATION
-------------

You can configure which templates to use. In your settings you can set:

    TABSPLUGIN_TEMPLATES = (
        ('template1.html', 'Template 1 Name'),
        ('template2.html', 'Template 2 Name'),
        .....
    )

By default cmsplugin-tabs use this configuration:

    TABSPLUGIN_TEMPLATES = (
        ('cmsplugin_tabs/tabs.html', 'Tabs'),
        ('cmsplugin_tabs/accordion.html', 'Accordion'),
    )


REQUIREMENTS
------------

Bootstrap 3

django-cmsplugin-tabs require django, django-cms and django-tinymce

Plugin was developed under Django ver 1.6 and Django-CMS ver 3.0 
