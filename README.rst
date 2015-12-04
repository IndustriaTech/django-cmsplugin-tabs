django-cmsplugin-tabs
=====================

Plugin for Django-CMS that create list of tabs

INSTALLATION
------------

You can simply install it with pip like this:

.. code-block:: bash

    pip install git+https://github.com/MagicSolutions/django-cmsplugin-tabs.git#egg=django-cmsplugin-tabs


After that you must add it to :code:`INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'cmsplugin_tabs',
        ...
    )

If you are using South you need to put add this in :code:`SOUTH_MIGRATION_MODULES`:

.. code-block:: python

    SOUTH_MIGRATION_MODULES = {
        ...
        'cmsplugin_tabs': 'cmsplugin_tabs.south_migrations',
        ...
    }


CONFIGURATION
-------------

You can configure which templates to use. In your settings you can set:

.. code-block:: python

    TABSPLUGIN_TEMPLATES = (
        ('template1.html', 'Template 1 Name'),
        ('template2.html', 'Template 2 Name'),
        .....
    )

By default cmsplugin-tabs use this configuration:

.. code-block:: python

    TABSPLUGIN_TEMPLATES = (
        ('cmsplugin_tabs/tabs.html', 'Tabs'),
        ('cmsplugin_tabs/accordion.html', 'Accordion'),
    )


REQUIREMENTS
------------

Bootstrap 3

django-cmsplugin-tabs require django, django-cms and django-ckeditor

Plugin was developed under Django ver 1.8 and DjangoCMS ver 3.1.

It should work on older versions of Django and DjangoCMS. Pull requests are welcome.
