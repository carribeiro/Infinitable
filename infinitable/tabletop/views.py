# coding: utf-8

from django.shortcuts import render_to_response
from django.http import Http404
from tabletop.models import Panel


def index(request):
    try:
        top_panel = Panel.objects.get(tag='index')
    except Panel.DoesNotExist:
        raise Http404
    return render_to_response('tabletop/index.html', {'top_panel': top_panel})
        
