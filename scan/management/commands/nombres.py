from django.core.management.base import BaseCommand, CommandError
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
                id = str(i.identificador)
                url = 'http://api.football-data.org/v2/teams/' + id
                response = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
                squad = json.loads(response.text)['squad']
                for p in squad:
                    if p['role'] == 'PLAYER':
                        nombre = p['name']
                        print(nombre)
                        player = Player.objects.get(name=str(p['id'])
                        player.words = nombre
                        player.save()
                        print('Updated player %s' % nombre)
                    time.sleep(2)    
            except Exception as e:
                print(e)
                pass
            print('CREATED PLAYERS FOR TEAM %s' % id)
    print('process finished')        
