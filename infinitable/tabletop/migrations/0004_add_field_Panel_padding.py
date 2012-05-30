# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Panel.padding'
        db.add_column('tabletop_panel', 'padding',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Panel.padding'
        db.delete_column('tabletop_panel', 'padding')


    models = {
        'tabletop.display': {
            'Meta': {'object_name': 'Display', '_ormbases': ['tabletop.Panel']},
            'panel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tabletop.Panel']", 'unique': 'True', 'primary_key': 'True'}),
            'slots': ('django.db.models.fields.IntegerField', [], {})
        },
        'tabletop.panel': {
            'Meta': {'object_name': 'Panel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'padding': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tabletop.Panel']"}),
            'tag': ('django.db.models.fields.TextField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['tabletop']