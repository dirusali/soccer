rom django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json
import time

urlteams = 'http://api.football-data.org/v2/competitions/2014/teams'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlteams, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        equipos = json.loads(r.text)['teams']
        teams = Team.objects.all()
        for i in teams:
            try:
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
             
            except Exception as e:
                print(e)
                pass
            print('CREATED PLAYERS FOR TEAM %s' % id)
    print('process finished')        
