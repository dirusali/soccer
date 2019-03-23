from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match


def partidos(request):
    qs = Match.objects.all()   
    qs = qs[0].local
    return HttpResponse(request, 'partidos.html', qs)
