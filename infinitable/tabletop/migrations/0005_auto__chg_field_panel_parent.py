# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Panel.parent'
        db.alter_column('tabletop_panel', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tabletop.Panel'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Panel.parent'
        raise RuntimeError("Cannot reverse this migration. 'Panel.parent' and its values cannot be restored.")

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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['tabletop.Panel']", 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.TextField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['tabletop']