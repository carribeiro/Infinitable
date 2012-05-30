# coding: utf-8
from django.db.models.base import Model
from django.db.models.fields import TextField, IntegerField
from django.db.models.fields.related import ForeignKey

class Panel(Model):
    tag = TextField(max_length=30)
    parent = ForeignKey('Panel')
    padding = IntegerField(default=2)

class Display(Panel):
    slots = IntegerField()
