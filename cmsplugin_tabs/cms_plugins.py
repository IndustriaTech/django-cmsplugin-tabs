from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CMSTabsList, CMSSingleTab, DEFAULT_TEMPLATE


class CMSTabsListPlugin(CMSPluginBase):
    model = CMSTabsList
    module = 'Tabs'
    name = 'Tabs'
    admin_preview = False
    render_template = DEFAULT_TEMPLATE
    allow_children = True
    child_classes = ["CMSSingleTabPlugin"]

    def render(self, context, instance, placeholder):
        self.render_template = instance.get_template()
        if len(instance.child_plugin_instances) >= 1:
            firstchild = instance.child_plugin_instances[0]
        else:
            firstchild = None
        context.update({
            'tabs_list_id': 'tabs_list_plugin_%s' % instance.pk,
            'firstchild': firstchild,
            'tabs': instance,
            })
        return context

plugin_pool.register_plugin(CMSTabsListPlugin)


class CMSSingleTabPlugin(CMSPluginBase):
    model = CMSSingleTab
    module = 'Tab'
    name = 'Tab'
    allow_children = True
    render_template = "cmsplugin_tabs/tab.html"
    parent_classes = ["CMSTabsListPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'tab': instance,
            })
        return context

plugin_pool.register_plugin(CMSSingleTabPlugin)
