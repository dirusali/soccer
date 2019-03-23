from django.http import HttpResponse
from django.shortcuts import render
from scan.models import Match, Team


def partidos(request):
    actual = 246112 + 280
    locals = []
    visitors = []
    qs = Match.objects.all()
    for i in range(actual, actual+10):
        p = Match.objects.get(matchid=i)
        locals.append(p.local.name)
        visitors.append(p.visitor.name)
    vista = {'matches':qs}
    return render(request, 'partidos.html', context=vista)
