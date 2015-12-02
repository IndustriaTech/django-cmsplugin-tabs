from django.conf import settings


# If slug in tabs is required or not
BLANK_SLUG = not getattr(settings, 'TABSPLUGIN_REQUIRE_SLUG', False)

# Possible templates for rendering the plugin
# It can look as tabs or as accordion by default
TEMPLATE_CHOICES = getattr(settings, 'TABSPLUGIN_TEMPLATES', (
    ('cmsplugin_tabs/tabs.html', 'Tabs'),
    ('cmsplugin_tabs/accordion.html', 'Accordion'),
))

# Default template is the first tempalte
DEFAULT_TEMPLATE = TEMPLATE_CHOICES[0][0]
