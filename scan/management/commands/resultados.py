from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json



class Command(BaseCommand):
    def handle(self, *args, **options):
        local_lineup_name = input("Indica la alineacion local: ")
        visitor_lineup_name = input("Indica la alineacion visitante: ")
        local = Lineups.objects.get(name=local_lineup_name)
        visitor = Lineups.objects.get(name=visitor_lineup_name)
        localplayers=Lineups.objects.get(name=local_lineup_name).values('players')
        visitorplayers = Lineups.objects.get(name=visitor_lineup_name).values('players')
        print('El equipo local juega con:')
        for i in localplayers:
            p =i.get('players',None)
            player = Players.objects.get(id=p.id)
            print(player.name)   
        print('El equipo visitante juega con:')
        for i in visitorplayers:
            p = i.get('players',None)
            player = Players.objects.get(id=p.id)
            print(player.name)
        

