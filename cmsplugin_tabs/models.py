from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from ckeditor.fields import RichTextField

REQUIRE_SLUG = getattr(settings, 'TABSPLUGIN_REQUIRE_SLUG', False)
TEMPLATE_CHOICES = getattr(settings, 'TABSPLUGIN_TEMPLATES', (
    ('cmsplugin_tabs/tabs.html', 'Tabs'),
    ('cmsplugin_tabs/accordion.html', 'Accordion'),
))
DEFAULT_TEMPLATE = TEMPLATE_CHOICES[0][0]


class CMSTabsList(CMSPlugin):
    template = models.CharField(_('Template'), max_length=255, choices=TEMPLATE_CHOICES, default=DEFAULT_TEMPLATE)

    class Meta:
        verbose_name = _('Tab list')
        verbose_name_plural = _('Tab lists')

    def get_template(self):
        return self.template or DEFAULT_TEMPLATE


class CMSSingleTab(CMSPlugin):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=32, blank=not REQUIRE_SLUG, default='')
    is_strong = models.BooleanField(_('Strong'), default=False, help_text='When True then label of the tab will be bold')
    content = RichTextField(_('Content'), blank=True, default='')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Tab')
        verbose_name_plural = _('Tabs')

    def get_html_id(self):
        return self.slug or 'cmsplugin_tabs_%s' % self.pk
