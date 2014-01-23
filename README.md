django-cmsplugin-tabs
=====================

Plugin for Django-CMS that create list of tabs (using jquery ui)

INSTALLATION
------------

You can simply install it with pip like this:

    pip install git+git://github.com/MagicSolutions/django-cmsplugin-tabs.git#egg=django-cmsplugin-tabs

After taht you must add it to installed apps:

    INSTALLED_APPS = (
        ...
        'cmsplugin-tabs',
        ...
    )

You must include JQuery and JQuery UI in your base template. Example:

    <link rel="stylesheet" type="text/css" href="http://code.jquery.com/ui/1.9.1/themes/base/jquery-ui.css">
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.8.2.js"></script>
    <script type="text/javascript" src="http://code.jquery.com/ui/1.9.1/jquery-ui.js"></script>


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
        ('cmsplugin_tabs/tabs.html', _('Tabs')),
        ('cmsplugin_tabs/accordion.html', _('Accordion')),
    )

NOTE: Actually `accordion.html` template will not work as expected, because there is no javascript for it.
But it will be easy to write custom JS and/or to change the template and make it work.


REQUIREMENTS
------------

django-cmsplugin-tabs require django and django-cms.

Plugin was developed under Django ver 1.3 and Django-CMS ver 2.2