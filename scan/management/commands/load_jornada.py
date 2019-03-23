
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup, Jornada

import requests
import json
import time

actual= 246112 + 28*10

class Command(BaseCommand):
    def handle(self, *args, **options):
        actuales = (actual, actual+10)
        print('LA JORNADA ACTUAL VA DEL PARTIDO %s al %s' % (actual,actual+10))
        for i in range(actual,actual+10):
            try:
                p = Match.objects.get(matchid=i)
                local = p.local.name
                visitante = p.visitor.name
                match = ('%s - %s' % (local,visitante))
                Jornada.objects.Create(currentmatch=match)
                partidos = []
                print('CREADO PARTIDO %s' % currentmatch)
            except Exception as e:
                print(e)
