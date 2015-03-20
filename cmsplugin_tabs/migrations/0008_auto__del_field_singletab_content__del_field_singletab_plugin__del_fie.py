# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SingleTab.content'
        db.delete_column(u'cmsplugin_tabs_singletab', 'content')

        # Deleting field 'SingleTab.plugin'
        db.delete_column(u'cmsplugin_tabs_singletab', 'plugin_id')

        # Deleting field 'SingleTab.id'
        db.delete_column(u'cmsplugin_tabs_singletab', 'id')

        # Deleting field 'SingleTab.order'
        db.delete_column(u'cmsplugin_tabs_singletab', 'order')

        # Adding field 'SingleTab.cmsplugin_ptr'
        db.add_column(u'cmsplugin_tabs_singletab', u'cmsplugin_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['cms.CMSPlugin'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SingleTab.content'
        db.add_column(u'cmsplugin_tabs_singletab', 'content',
                      self.gf('tinymce.models.HTMLField')(default=''),
                      keep_default=False)

        # Adding field 'SingleTab.plugin'
        db.add_column(u'cmsplugin_tabs_singletab', 'plugin',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='tab', related_name='tabs', to=orm['cmsplugin_tabs.CMSTabsList']),
                      keep_default=False)

        # Adding field 'SingleTab.id'
        db.add_column(u'cmsplugin_tabs_singletab', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=datetime.datetime(2015, 3, 19, 0, 0), primary_key=True),
                      keep_default=False)

        # Adding field 'SingleTab.order'
        db.add_column(u'cmsplugin_tabs_singletab', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Deleting field 'SingleTab.cmsplugin_ptr'
        db.delete_column(u'cmsplugin_tabs_singletab', u'cmsplugin_ptr_id')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'cmsplugin_tabs.cmstabslist': {
            'Meta': {'object_name': 'CMSTabsList', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_tabs/tabs.html'", 'max_length': '255'})
        },
        u'cmsplugin_tabs.singletab': {
            'Meta': {'object_name': 'SingleTab', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'is_strong': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_tabs']