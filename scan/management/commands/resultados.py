from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json



class Command(BaseCommand):
    def handle(self, *args, **options):
        local_lineup_name = input("Indica la alineacion local:")
        visitor_lineup_name = input("Indica la alineacion visitante:")
        print('has elegido el local: %s' % (local_lineup_name))
        print('has elegido el visitante: %s' % (visitor_lineup_name))
        local = Lineup.objects.get(name=local_lineup_name)
        visitor = Lineup.objects.get(name=visitor_lineup_name)
        localplayers=Lineup.objects.filter(name=local_lineup_name).values('players')
        visitorplayers = Lineup.objects.filter(name=visitor_lineup_name).values('players')
        print('El equipo local juega con:')
        for i in localplayers:
            p =i.get('players',None)
            player = Player.objects.get(id=p)
            print(player.name)   
        print('El equipo visitante juega con:')
        for i in visitorplayers:
            p = i.get('players',None)
            player = Player.objects.get(id=p)
            print(player.name)
        

