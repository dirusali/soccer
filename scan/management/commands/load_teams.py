from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json

url = 'http://api.football-data.org/v2/competitions/2014/teams?season=2016'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        equipos = json.loads(r.text)['teams']
        count = 0
        for i in equipos:
            count+=1
            nombre = i['name']
            id = i['id']
            try:
                Team.objects.get(name=nombre)
                print('YA ESTA CREADO')
                pass
            except:    
                Team.objects.create(name= nombre,identificador=id)
                print('CREATED TEAM %s' % nombre)
    print('process finished')        
        
