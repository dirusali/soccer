from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match


def partidos(request):
    actual = 246112 + 280
    locals = []
    visitors = []
    qs = Match.objects.all()
    for i in range(actual, actual+10):
        p = Match.objects.get(matchid=i)
        locals.append(p.local)
        visitors.append(i.visitor)
    vista = {'matches':qs}
    return render(request, 'partidos.html', context=vista)
