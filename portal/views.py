from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match


def partidos(request):
    pasada = 28
    inicio = 246112
    actual = 246112 + pasada*10
    locals = []
    visitors = []
    qs = Match.objects.all()
    for i in range(actual, actual+10):
        p = Match.objects.get(id=i)
        locals.append(p.local)
        visitors.append(i.visitor)
    vista = {'matches':qs}
    return render(request, 'partidos.html', context=vista)
