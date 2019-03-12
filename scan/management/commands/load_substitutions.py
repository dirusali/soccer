rom django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json
import time

urlmatches = 'http://api.football-data.org/v2/competitions/2014/matches'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlmatches, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        matches = json.loads(r.text)['matches']
        time.sleep(11)
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
                print('PROCEDIENDO A AÑADIR SUSTITUCIONES')
                s = json.loads(r.text)['match']['substitutions']
                l = json.loads(r.text)['match']['homeTeam']['name']
                v = json.loads(r.text)['match']['awayTeam']['name']
                homelineup = json.loads(r.text)['match']['homeTeam']['lineup']
                awaylineup =  json.loads(r.text)['match']['awayTeam']['lineup']
                codigolocal = []
                codigovisitante = []
                for h in homelineup:
                    codigolocal.append(str(h['id'])[0])
    
                for v in awaylineup:
                    codigovisitante.append(str(v['id'])[0])
    
                local_lineup = Lineup.objects.get(lineupid=codigolocal)
                visitor_lineup = Lineup.objects.get(lineupid=codigovisitante)
                ls = []
                vs = []
                for i in substitutions:
                    team = i['team']['name']    
                    if team == local:
                        ls.append(ls)
                    if team == visitor:
                        vs.append(vs)
        
                for i in ls:
                    time = i['minute']
                    tl.append(time)
                for i in vs:
                    time = i['minute']
                    tv.append(time)

                localtimes = [y - x for x,y in zip(tl,tl[1:])]
                visitortimes = [y - x for x,y in zip(tv,tv[1:])]   

                newlocallineups = []
                newvisitorlineuos = []

                for i in ls:        
                    sale = str(i['playerOut']['id'][0])
                    entra = str(i['playerIn']['id'][0])
                    newlineup = codigolocal.remove(sale)
                    newlineup = codigolocal.append(entra)
                    Lineup.objects.create(players=codigolocal, team=local)
        
        
                for i in vs:
                    sale = str(i['playerOut']['id'])
                    entra = str(i['playerIn']['id'])
                    codigovisitante.remove(sale)
                    codigovisitante.append(entra)
                             
                             
