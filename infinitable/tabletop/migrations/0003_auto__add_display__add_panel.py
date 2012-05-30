# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Display'
        db.create_table('tabletop_display', (
            ('panel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tabletop.Panel'], unique=True, primary_key=True)),
            ('slots', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tabletop', ['Display'])

        # Adding model 'Panel'
        db.create_table('tabletop_panel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tabletop.Panel'])),
        ))
        db.send_create_signal('tabletop', ['Panel'])


    def backwards(self, orm):
        # Deleting model 'Display'
        db.delete_table('tabletop_display')

        # Deleting model 'Panel'
        db.delete_table('tabletop_panel')


    models = {
        'tabletop.display': {
            'Meta': {'object_name': 'Display', '_ormbases': ['tabletop.Panel']},
            'panel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tabletop.Panel']", 'unique': 'True', 'primary_key': 'True'}),
            'slots': ('django.db.models.fields.IntegerField', [], {})
        },
        'tabletop.panel': {
            'Meta': {'object_name': 'Panel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tabletop.Panel']"}),
            'tag': ('django.db.models.fields.TextField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['tabletop']