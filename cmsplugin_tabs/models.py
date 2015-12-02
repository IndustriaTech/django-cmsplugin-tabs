from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from ckeditor.fields import RichTextField

from .utils import force_str, force_text


from .conf import TEMPLATE_CHOICES, DEFAULT_TEMPLATE, BLANK_SLUG


class CMSTabsList(CMSPlugin):
    template = models.CharField(_('Template'), max_length=255, choices=TEMPLATE_CHOICES, default=DEFAULT_TEMPLATE)

    class Meta:
        verbose_name = _('Tab list')
        verbose_name_plural = _('Tab lists')

    def __str__(self):
        return force_str(self.get_template_display())

    def __unicode__(self):
        return force_text(self.get_template_display())

    def get_template(self):
        return self.template or DEFAULT_TEMPLATE


class CMSSingleTab(CMSPlugin):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=32, blank=BLANK_SLUG, default='')
    is_strong = models.BooleanField(_('Strong'), default=False, help_text='When True then label of the tab will be bold')
    content = RichTextField(_('Content'), blank=True, default='')

    def __str__(self):
        return force_str(self.title)

    def __unicode__(self):
        return force_text(self.title)

    class Meta:
        verbose_name = _('Tab')
        verbose_name_plural = _('Tabs')

    def get_html_id(self):
        return self.slug or 'cmsplugin_tabs_%s' % self.pk
