from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models import CMSPlugin
from tinymce.models import HTMLField


class CMSTabsList(CMSPlugin):

    def copy_relations(self, oldinstance):
        super(CMSTabsList, self).copy_relations(oldinstance)
        for tab in oldinstance.tabs.all().iterator():
            tab.pk = None
            tab.plugin = self
            tab.save()


class SingleTab(models.Model):
    plugin = models.ForeignKey(CMSTabsList, related_name='tabs')
    title = models.CharField(_('Title'), max_length=64)
    content = HTMLField(_('Content'))
    order = models.PositiveIntegerField(_('Order'), default=1, db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name = _('Tab')
        verbose_name_plural = _('Tabs')

    def __unicode__(self):
        return unicode(self.title)

    def get_html_id(self):
        return 'cmsplugin_tabs_%s' % self.pk
