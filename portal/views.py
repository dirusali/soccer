from django.http import HttpResponse
from django.shortcuts import Render
from scan.models import Match

from templates.py import partidos.html

def partidos(request):
    qs = Match.objects.all()        
    vista = {"partidos": qs}
    return HttpResponse(request, partidos.html, context=vista)
