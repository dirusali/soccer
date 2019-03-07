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
                print('BUSCANDO EL PARTIDO CON URL %s' % url)
                r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
                l = json.loads(r.text)['match']['homeTeam']['name']
                v = json.loads(r.text)['match']['awayTeam']['name']
                print('EL EQUIPO LOCAL ES %s' % local)
                print('EL EQUIPO VISITANTE ES %s' % visitor)
                casa = Team.objects.get(name=l)
                fuera = Team.objects.get(name=v)
                print('CREANDO PARTIDO CON EKIPOS %s Y %s' % (casa,fuera))
                Match.objects.create(matchid=i, local=casa, visitor=fuera)
                print('CREADO EL PARTIDO %s' % (Match.matchid))
                sleep(11)
            except Exception as e:
                print(e)
                pass
            
        print('finito')    
    
    
        
                
        
