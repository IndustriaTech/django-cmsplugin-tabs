from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from cms.models import CMSPlugin
from tinymce.models import HTMLField

REQUIRE_SLUG = getattr(settings, 'TABSPLUGIN_REQUIRE_SLUG', False)
TEMPLATE_CHOICES = getattr(settings, 'TABSPLUGIN_TEMPLATES', (
    ('cmsplugin_tabs/tabs.html', _('Tabs')),
    ('cmsplugin_tabs/accordion.html', _('Accordion')),
))
DEFAULT_TEMPLATE = TEMPLATE_CHOICES[0][0]


class CMSTabsList(CMSPlugin):
    template = models.CharField(_('Template'), max_length=255, choices=TEMPLATE_CHOICES, default=DEFAULT_TEMPLATE)

    def copy_relations(self, oldinstance):
        super(CMSTabsList, self).copy_relations(oldinstance)
        for tab in oldinstance.tabs.all().iterator():
            tab.pk = None
            tab.plugin = self
            tab.save()

    def get_template(self):
        return self.template or DEFAULT_TEMPLATE


class SingleTab(models.Model):
    plugin = models.ForeignKey(CMSTabsList, related_name='tabs')
    title = models.CharField(_('Title'), max_length=255)
    content = HTMLField(_('Content'))
    slug = models.SlugField(_('Slug'), max_length=32, blank=not REQUIRE_SLUG, default='')
    order = models.PositiveIntegerField(_('Order'), default=1, db_index=True)
    is_strong = models.BooleanField(_('Strong'), default=False, help_text=_('When True then label of the tab will be bold'))

    class Meta:
        ordering = ['order']
        verbose_name = _('Tab')
        verbose_name_plural = _('Tabs')

    def __unicode__(self):
        return unicode(self.title)

    def get_html_id(self):
        return self.slug or 'cmsplugin_tabs_%s' % self.pk
