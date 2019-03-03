from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json

urlteams = 'http://api.football-data.org/v2/competitions/2014/teams'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlteams, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        equipos = json.loads(r.text)['teams']
        teams = Team.objects.all()
        for i in teams:
            id = str(i.identificador)
            url = 'http://api.football-data.org/v2/teams/' + id
            response = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
            squad = json.loads(response.text)['squad']
            for p in squad:
                if p['role'] == 'PLAYER':
                    edad = 2019 - int(p['dateOfBirth'][0:4])
                    i.player_set.create(
                    name=i['name'],
                    position=i['position'],
                    age=edad)
                    i.save()
                    print('Created player %s' % name)
            print('CREATED PLAYERS FOR TEAM %s' % id)
    print('process finished')        
