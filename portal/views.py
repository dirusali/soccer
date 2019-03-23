from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match


def partidos(request):
    vista = {'variable':'vengo de vistas')
    return HttpResponse(request, 'templates/partidos.html', context=vista)
