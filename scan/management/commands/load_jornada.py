
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup, Jornada

import requests
import json
import time

urlteams = 'http://api.football-data.org/v2/competitions/2014/matches'
actual=28*10

class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlteams, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        actuales = (actual, actual+10)
        for i in range(actual,actual+10):
            p = Match.objects.get(matchid=i)
            local = p.local.name
            visitante = p.visitante.name
            match = ('%s - %s' % (local,visitante))
            Jornada.objects.Create(currentmatch=match)
            partidos = []
            print('CREADO PARTIDO %s' % currentmatch)
            
