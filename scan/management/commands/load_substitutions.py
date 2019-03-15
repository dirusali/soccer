from django.core.management.base import BaseCommand, CommandError
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
                localplayers = []
                visitorplayers = []
                for h in homelineup:
                    codigolocal.append(str(h['id']))
    
                for v in awaylineup:
                    codigovisitante.append(str(v['id']))
    
                local_lineup = Lineup.objects.get(lineupid=codigolocal)
                visitor_lineup = Lineup.objects.get(lineupid=codigovisitante)
                ls = []
                vs = []
                
                for i in s:
                    team = i['team']['name']    
                    if team == l:
                        ls.append(ls)
                    if team == v:
                        vs.append(vs)
        
                for i in ls:
                    time = i['minute']
                    tl.append(time)
                for i in vs:
                    time = i['minute']
                    tv.append(time)

                localtimes = [y - x for x,y in zip(tl,tl[1:])]
                visitortimes = [y - x for x,y in zip(tv,tv[1:])]   
                local_lineup.timeplayed = local_lineup.timeplated + localtimes[0]
                print('AÑADIDO TIEMPO1 DE ALINEACION LOCAL %s' % localtimes[0])
                local_lineup.save()
                visitor_lineup.timeplayed = visitor_lineuo.timeplated + visitortimes[0]
                print('AÑADIDO TIEMPO1 DE ALINEACION VISITANTE %s' % visitortimes[0])
                visitor_lineup.save()
                
                count= 0
                for i in ls:
                    count+=1
                    sale = str(i['playerOut']['id'])
                    print('SALE EL JUGADOR %s' % sale)
                    entra = str(i['playerIn']['id'])
                    print('ENTRA EL JUGADOR %s' % entra)
                    codigolocal = codigolocal.remove(sale)
                    codigolocal = codigolocal.append(entra)
                    for p in codigolocal:
                        try:
                            player = Player.objects.get(name=str(p))
                        except:
                            Player.objects.create(name = str(p), team=l)
                            print('Creado el jugador %s' % p)
                            player = Player.objects.get(name=str(p))                        
                        localplayers.append(player)
                    nueva = Lineup.objects.create(lineupid = codigolocal, players=codigolocal, team=l, timeplayed = localtimes[count])
                    print('CREADA NUEVA LINEUP %s' % nueva.lineupid)

        
                count = 0
                for i in vs:
                    count+=1
                    sale = str(i['playerOut']['id'])
                    print('SALE EL JUGADOR %s' % sale)
                    entra = str(i['playerIn']['id'])
                    print('ENTRA EL JUGADOR %s' % entra)
                    codigovisitante.remove(sale)
                    codigovisitante.append(entra)
                    for p in codigovisitante:
                        try:
                            player = Player.objects.get(name=str(p))
                        except:
                            Player.objects.create(name = str(p), team=v)
                            print('Creado el jugador %s' % p)
                            player = Player.objects.get(name=str(p))                        
                        visitorplayers.append(player)
                    nueva = Lineup.objects.create(lineupid = codigolocal, players=codigolocal, team=v, timeplayed = visitortimes[count])
                    print('CREADA NUEVA LINEUP %s' % nueva.lineupid)
                             
                             
