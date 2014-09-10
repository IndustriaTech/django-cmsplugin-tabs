from django.utils.translation import ugettext as _
from django.contrib.admin import StackedInline

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CMSTabsList, SingleTab, DEFAULT_TEMPLATE


class TabInline(StackedInline):
    model = SingleTab
    extra = 1
    prepopulated_fields = {"slug": ("title",)}


class CMSTabsListPlugin(CMSPluginBase):
    model = CMSTabsList
    module = _('Tabs')
    name = _('Tabs')
    admin_preview = False
    render_template = DEFAULT_TEMPLATE
    inlines = [TabInline]

    class Media:
        js = (
            "cmsplugin_tabs/js/jquery.init.js",
            "cms/js/libs/jquery.ui.core.js",
            "cms/js/libs/jquery.ui.sortable.js",
            "cmsplugin_tabs/js/jquery.inlineordering.js",
            )

    def render(self, context, instance, placeholder):
        self.render_template = instance.get_template()
        context.update({
            'tabs_list_id': 'tabs_list_plugin_%s' % instance.pk,
            'tabs': instance.tabs.all(),
            })
        return context

plugin_pool.register_plugin(CMSTabsListPlugin)
