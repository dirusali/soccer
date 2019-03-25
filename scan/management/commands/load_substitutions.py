from django.core.management.base import BaseCommand, CommandError
from django.db import models
from scan.models import Competition, Match, Team, Player, Lineup

import requests
import json
from time import sleep

urlmatches = 'http://api.football-data.org/v2/competitions/2014/matches/2017'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(urlmatches, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
        matches = json.loads(r.text)['matches']
        sleep(1)
        partidos = []
        for i in matches:
            try:
                p = i['id']
                partidos.append(p)
            except:
                pass    
        for i in partidos:
            try:
                sleep(5)
                url = 'http://api.football-data.org/v2/matches/' + str(i)
                print('BUSCANDO EL PARTIDO CON URL %s' % url)
                r = requests.get(url, headers={'X-Auth-Token':'dfec1fbedad7421abdad5eda2372b4c2'})
                print('---------------llamando API-----------------------')
                subs = json.loads(r.text)['match']['substitutions']
                l = json.loads(r.text)['match']['homeTeam']['name']
                v = json.loads(r.text)['match']['awayTeam']['name']
                homelineup = json.loads(r.text)['match']['homeTeam']['lineup']
                awaylineup =  json.loads(r.text)['match']['awayTeam']['lineup']
                print('EL EKIPO LOCAL ES %s' % l)
                print('EL VISITANTE ES %s' % v)
                print('EL NUMERO DE CAMBIOS ES %s' % len(subs))
                local = Team.objects.get(name=l)
                visitor = Team.objects.get(name=v)
                codigolocal = ''
                codigovisitante = ''
                localplayers = []
                visitorplayers = []            
                ls = []
                vs = []
                tl = []
                tv = []
                lg = []
                vg = []
                tlg = []
                tvg = []
                localtimes = []
                visitortimes = []
                listalocal = []
                listavisitante = []
                localgoaltimes = []
                visitorgoaltimes = []
              
                for h in homelineup:
                    codigolocal+=str(h['id'])
                    listalocal.append(str(h['id']))
                
                for w in awaylineup:
                    codigovisitante+=str(w['id'])
                    listavisitante.append(str(w['id']))
                
                print('EL CODIGO LOCAL ES %s' % codigolocal)
                print('EL CODIGO VISITANTE ES %s' % codigovisitante)
             
                try:
                    local_lineup = Lineup.objects.get(lineupid=codigolocal)
                except:
                    players = []
                    Lineup.objects.create(lineupid=codigolocal, team= local, timeplayed=0, goalsfavor=0, goalscounter=0)
                    local_lineup = Lineup.objects.get(lineupid=codigolocal)
                    for p in homelineup:
                        try:
                            player = Player.objects.get(name=str(p['id']))
                        except:
                            player = Player.objects.create(name = str(p['id']), team=local)
                            print('Creado el jugador %s' % i)
                        players.append(player) 
                    local_lineup.players = players
                    local_lineup.save()                                                     
                print('EL NOMBRE DE LA ALINEACION LOCAL ES %s' % local_lineup.lineupid)    
                                                        
                try:
                    visitor_lineup = Lineup.objects.get(lineupid=codigovisitante)
                except:
                    players = []
                    Lineup.objects.create(lineupid=codigovisitante, team= visitor, timeplayed=0, goalsfavor=0, goalscounter=0)
                    visitor_lineup = Lineup.objects.get(lineupid=codigovisitante)
                    for p in awaylineup:
                        try:
                            player = Player.objects.get(name=str(p['id']))
                        except:
                            player = Player.objects.create(name = str(p['id']), team=visitor)
                            print('Creado el jugador %s' % i)
                        players.append(player)  
                    visitor_lineup.players = players
                    visitor_lineup.save()                                                                                                           
               
                print('EL NOMBRE DE LA ALINEACION VISITANTE ES %s' % visitor_lineup.lineupid)
                print('el tiempo default visitor es %s' % visitor_lineup.timeplayed)     
                
                for i in subs:
                    team = i['team']['name']
                    if team == l:
                        ls.append(i)
                        print('añadido %s' % l)
                    if team == v:
                        vs.append(i)
                        print('añadido %s' % v)
                        
                for i in ls:
                    time = i['minute']
                    tl.append(time)
                    
                for i in vs:
                    time = i['minute']
                    tv.append(time)
            except Exception as e:
                print(e)
                pass
            
            
            print('los cambios locales son en %s y los visitantes en %s' % (tl, tv))    
           
            try:    
                goals = json.loads(r.text)['match']['goals']
                if len(goals) > 0:
                    print('los goles son %s' % goals) 
                
                    for i in goals:
                        team = i['team']['name']  
                        print(team)
                        if team == l:
                            lg.append(i)
                        if team == v:
                            vg.append(i)
                    print(lg)
                    print(vg)
                    if len(lg) > 0:
                        for i in lg:
                            time = i['minute']
                            tlg.append(time)
                    if len(vg) > 0:
                        for i in vg:
                            time = i['minute']
                            tvg.append(time)  
                print('los goles locales son en %s y los visitantes en %s' % (tlg,tvg))    
        
            except Exception as e:
                print(e)
                pass
            
            
            try:
                tl.append(93)
                tv.append(93)
                print(tl)
                print(tv)
                if len(tl) > 1:
                    localtimes = [y - x for x,y in zip(tl,tl[1:])]
                if len(tv) > 1:
                    visitortimes = [y - x for x,y in zip(tv,tv[1:])]                  
                local_lineup.timeplayed  = local_lineup.timeplayed + tl[0]
                print('AÑADIDO TIEMPO1 DE ALINEACION LOCAL %s' % tl[0])
                local_lineup.save()
                print('AHORA EL VISITANTE')
                visitor_lineup.timeplayed = visitor_lineup.timeplayed + tv[0]
                print('AÑADIDO TIEMPO1 DE ALINEACION VISITANTE %s' % tv[0])
                visitor_lineup.save()
                
                print('AHORA VAMOS A AÑADIR LOS GOLES')
                print(tlg)
                localgoaltimes = tlg
                count = 0
                if len(tlg) > 0:
                    for goal in tlg:
                        if goal < tl[0]:
                            count+=1
                            local_lineup.goalsfavor = local_lineup.goalsfavor + 1 
                            localgoaltimes = localgoaltimes[1:]
                            visitor_lineup.goalscounter = visitor_lineup.goalscounter + 1
                            print('GOL PRIMERA ALINEACION')
                            print(localgoaltimes)
                            local_lineup.save()
                            visitor_lineup.save()
                            print('QUITO GOL')
                        else:
                            print('GOLES DE OTRA ALINEACION')
             
            except Exception as e:
                print(e)
            
            try:    
                count = 0
                print(tvg)
                visitorgoaltimes = tvg
                if len(tvg) > 0:
                    for goal in tvg:
                        if goal < tv[0]:
                            count+=1
                            visitor_lineup.goalsfavor = visitor_lineup.goalsfavor + 1 
                            local_lineup.goalscounter = local_lineup.goalscounter + 1
                            visitoegoaltimes = visitorgoaltimes[1:]
                            local_lineup.save()
                            visitor_lineup.save()
                            print('GOL PRIMERA ALINEACION')
                            print(visitorgoaltimes)
                            print('QUITO GOL')
                        else:
                            print('GOLES DE OTRA ALINEACION')
            except Exception as e:
                print(e)
                pass
            
            print('AHORA ACTUALIZAMOS GOLES Y CAMBIOS EN EL EQUIPO LOCAL')
                
            try:
                count= 0
                for i in ls:
                    count+=1
                    limitsup = tl[count]
                    limitinf = tl[count-1]
                    tiempo = limitsup - limitinf
                    print('CREANDO LA ALINEACION QUE JUGÓ ENTRE MIN %s Y EL MIN  %s' % (limitinf,limitsup)) 
                    sale = str(i['playerOut']['id'])
                    print('SALE EL JUGADOR %s' % sale)
                    entra = str(i['playerIn']['id'])
                    print('ENTRA EL JUGADOR %s' % entra)
                    codigolocal = codigolocal.replace(sale, '')
                    codigolocal = codigolocal + entra
                    try:
                        nueva = Lineup.objects.get(lineupid=codigolocal)
                        print('ALINEACION ENCONTRADA')
                        psale = Player.objects.get(name=sale)
                        pentra = Player.objects.get(name=entra)
                        nueva.players.remove(psale)
                        nueva.players.add(pentra)
                        nueva.save()
                        print('CREADA ALINEACION')
                    except:
                        print('NO EXISTE ALINEACION, CREANDOLA....')
                        listalocal.remove(sale)
                        listalocal.append(entra)
                        players = []
                        for p in listalocal:
                            try:
                                player = Player.objects.get(name=p)
                                players.append(player)
                                #print('AÑADIDO JUGADOR')
                            except:
                                Player.objects.create(name = p, team=local)
                                print('Creado el jugador %s' % p)
                                player = Player.objects.get(name=p)                        
                                players.append(player)
                                #print('AÑADIDO JUGADOR')
                        print('los players son %s' % len(players))        
                        print('EL TIEMPO PARA ESTA ALINEACION ES %s' % tiempo)    
                        Lineup.objects.create(lineupid = codigolocal, team=local, timeplayed = tiempo)
                        nueva = Lineup.objects.get(lineupid=codigolocal)
                        nueva.players = players
                        nueva.save()
                        print('CREADA ALINEACION')
                    if len(localgoaltimes) > 0:
                        for goal in localgoaltimes:
                            if goal in range(limitinf, limitsup):
                                nueva.goalsfavor = nueva.goalsfavor + 1
                                print('GOL AÑADIDO A FAVOR')
                    if len(visitorgoaltimes) > 0:
                        for goal in visitorgoaltimes:
                            if goal in range(limitinf, limitsup):
                                nueva.goalscounter = nueva.goalscounter + 1
                                print('GOL AÑADIDO EN CONTRA')        
                    nueva.save()            
                print('CREADA NUEVA LINEUP %s' % nueva.lineupid)
            except Exception as e:
                print(e)
                pass
            print('AHORA ACTUALIZAMOS GOLES Y CAMBIOS EN EL EQUIPO VISINTATE')

            try:
                count = 0
                for i in vs:
                    count+=1
                    limitsup = tv[count]
                    limitinf = tv[count-1]
                    tiempo = limitsup - limitinf
                    print('CREANDO LA ALINEACION QUE JUGÓ ENTRE MIN %s Y EL MIN  %s' % (limitinf,limitsup)) 
                    sale = str(i['playerOut']['id'])
                    print('SALE EL JUGADOR %s' % sale)
                    entra = str(i['playerIn']['id'])
                    print('ENTRA EL JUGADOR %s' % entra)
                    codigovisitante = codigovisitante.replace(sale, '')
                    codigovisitante = codigovisitante + entra
                    try:
                        nueva = Lineup.objects.get(lineupid=codigovisitante)
                        print('ALINEACION ENCONTRADA')
                        psale = Player.objects.get(name=sale)
                        pentra = Player.objects.get(name=entra)
                        nueva.players.remove(psale)
                        nueva.players.add(pentra)
                        nueva.save()
                    except:
                        print('NO EXISTE ALINEACION, CREANDOLA....')
                        listavisitante.remove(sale)
                        listavisitante.append(entra)
                        players = []
                        for p in listavisitante:
                            try:
                                player = Player.objects.get(name=p)
                                players.append(player)
                                #print('AÑADIDO JUGADOR')
                            except:
                                Player.objects.create(name = p, team=visitor)
                                print('Creado el jugador %s' % p)
                                player = Player.objects.get(name=p)                        
                                players.append(player)
                                #print('AÑADIDO JUGADOR')
                        print('los players son %s' % len(players))        
                        print('EL TIEMPO PARA ESTA ALINEACION ES %s' % tiempo)    
                        Lineup.objects.create(lineupid = codigovisitante, team=visitor, timeplayed = tiempo)
                        nueva = Lineup.objects.get(lineupid=codigovisitante)
                        nueva.players = players
                        nueva.save()
                    if len(visitorgoaltimes) > 0:
                        for goal in visitorgoaltimes:
                            if goal in range(limitinf, limitsup):
                                nueva.goalsfavor = nueva.goalsfavor + 1
                                print('GOL AÑADIDO A FAVOR')
                    if len(localgoaltimes) > 0:
                        for goal in localgoaltimes:
                            if goal in range(limitinf, limitsup):
                                nueva.goalscounter = nueva.goalscounter + 1
                                print('GOL AÑADIDO EN CONTRA')        
                    nueva.save()
                print('CREADA NUEVA LINEUP %s' % nueva.lineupid)
            except Exception as e:
                print(e)
                pass
                  
        print('TERMINADAS TODAS LAS SUSTITUCIONES')                     
