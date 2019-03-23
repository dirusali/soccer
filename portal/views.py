from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match


def partidos(request):
    qs = 'local'
    return HttpResponse(request, 'templates/partidos.html', qs)
