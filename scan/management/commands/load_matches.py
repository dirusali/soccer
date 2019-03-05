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
        r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        matches = json.loads(r.text)['matches']
        partidos = []
        for i in matches:
            p = i['id']
            partidos.append(p)
        for i in partidos:
            url = 'http://api.football-data.org/v2/matches/' + str(i)
            r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
            local = json.loads(r.text)['homeTeam']['name']
            visitor = json.loads(r.text)['homeTeam']['name']
            localteam = Team.objects.get(name=local)
            visitorteam = Team.objects.get(name=visitor)
            Match.create(matchid=i['id'], local=local, visitor=visitorteam)
            print('CREADO EL PARTIDO CON LOS EQUIPOS %s' % (local,visitorteam))
            
            print('PROCEDIENDO A AÑADIR ALINEACIONES')
            local_lineup = []
            visitor_lineup = []
            homelineup = json.loads(r.text)['homeTeam']['lineup']
            awaylineup =  json.loads(r.text)['homeTeam']['lineup']
            alineacioneslocal = localteam.lineup_set.all()
            alineacionesvisitante = visitorteam.lineup_set.all()
            for h in homelineup:
                local_lineup.append(h['id'])
            for v in awaylineup:
                visitor_lineup.append(v['id'])
        
            for a in alineacioneslocal:
                if a.players != local_lineup:
                    Team.lineup.create(players=local_lineup)
                else:
                    print('ESTA ALINEACION YA EXISTE)
            for a in alineacionesvisitante:
                if a.players =! visitor_lineup:
                    Team.lineup.create(players=visitor_lineup)
            
    
    
        
                
        
