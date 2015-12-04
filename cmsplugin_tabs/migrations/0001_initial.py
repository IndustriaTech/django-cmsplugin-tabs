# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields

from cmsplugin_tabs.conf import BLANK_SLUG, TEMPLATE_CHOICES, DEFAULT_TEMPLATE


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSSingleTab',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('slug', models.SlugField(verbose_name='Slug', default='', max_length=32, blank=BLANK_SLUG)),
                ('is_strong', models.BooleanField(default=False, verbose_name='Strong', help_text='When True then label of the tab will be bold')),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Tab',
                'verbose_name_plural': 'Tabs',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CMSTabsList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, to='cms.CMSPlugin', parent_link=True)),
                ('template', models.CharField(verbose_name='Template', default=DEFAULT_TEMPLATE, choices=TEMPLATE_CHOICES, max_length=255)),
            ],
            options={
                'verbose_name': 'Tab list',
                'verbose_name_plural': 'Tab lists',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
