from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match


def partidos(request):
    qs = Match.objects.all()        
    vista = {"partidos": qs}
    return HttpResponse(request, partidos.html, context=vista)
