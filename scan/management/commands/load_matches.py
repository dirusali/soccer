from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json
import time

urlteams = 'http://api.football-data.org/v2/competitions/2014/matches'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlteams, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        matches = json.loads(r.text)['matches']
        partidos = []
        for i in matches:
            try:
                p = i['id']
                partidos.append(p)
            except:
                pass    
        for i in partidos:
            try:
                url = 'http://api.football-data.org/v2/matches/' + str(i)
                r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
                local = json.loads(r.text)['homeTeam']['name']
                visitor = json.loads(r.text)['homeTeam']['name']
                localteam = Team.objects.get(name=local)
                visitorteam = Team.objects.get(name=visitor)
                Match.create(matchid=i['id'], local=local, visitor=visitorteam)
                print('CREADO EL PARTIDO CON LOS EQUIPOS %s' % (local,visitorteam))
            except Exception as e:
                print(e)
                pass
            
        print('finito')    
    
    
        
                
        
